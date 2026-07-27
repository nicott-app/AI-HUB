"""
Implementación de TicketRepository sobre Firebase Firestore.

Si en el futuro se migra a otra base de datos (Supabase, PostgreSQL, etc.),
solo hay que crear una nueva clase que implemente TicketRepository, sin tocar
la UI ni los servicios.
"""
import os
import logging
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Any, Optional

import firebase_admin
from firebase_admin import credentials, firestore

from src.repositories.ticket_repository import TicketRepository
from src.models.agile import Epic, UserStory
from src.config import (
    TICKET_QUERY_LIMIT, EPIC_TYPES, STORY_TYPES,
    DONE_STATUSES, MAX_PARALLEL_WORKERS
)

logger = logging.getLogger(__name__)


class FirebaseRepository(TicketRepository):
    """Implementación concreta del repositorio usando Firebase Firestore."""

    _instance = None
    _db = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self) -> None:
        if not firebase_admin._apps:
            try:
                import json
                cred_dict = None

                # 1. Streamlit Secrets — formato sección [firebase] (más fiable en la nube)
                try:
                    import streamlit as st
                    if "firebase" in st.secrets:
                        cred_dict = dict(st.secrets["firebase"])
                    elif "FIREBASE_CREDENTIALS" in st.secrets:
                        raw = st.secrets["FIREBASE_CREDENTIALS"]
                        cred_dict = json.loads(raw) if isinstance(raw, str) else dict(raw)
                except Exception:
                    pass

                # 2. Variable de entorno (fallback)
                if not cred_dict:
                    env_cred = os.getenv("FIREBASE_CREDENTIALS")
                    if env_cred:
                        cred_dict = json.loads(env_cred)

                # 3. Archivo local (desarrollo)
                if cred_dict:
                    cred = credentials.Certificate(cred_dict)
                else:
                    cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH", "./firebase-credentials.json")
                    if os.path.exists(cred_path):
                        cred = credentials.Certificate(cred_path)
                    else:
                        cred = credentials.ApplicationDefault()

                firebase_admin.initialize_app(cred)
                self._db = firestore.client()
                logger.info("Firebase inicializado correctamente.")

            except Exception as e:
                logger.error(f"No se pudo inicializar Firebase: {e}")
        else:
            if self._db is None:
                self._db = firestore.client()

    # ─── Helpers privados ─────────────────────────────────────────────────────

    def _tickets_ref(self, project_id: str):
        return self._db.collection("projects").document(project_id).collection("tickets")

    def _now_iso(self) -> str:
        return datetime.now(timezone.utc).isoformat()

    def _display_id(self, doc_id: str, data: dict) -> str:
        """Devuelve el ID visible en el tablero con este orden de prioridad:
        1. El campo 'code' del documento (ej: TKT-55)
        2. El propio doc_id si tiene formato de tablero (ej: DA-027)
        3. El doc_id como fallback.
        """
        if data.get("code"):
            return data["code"]
        parts = doc_id.split("-")
        if len(parts) == 2 and parts[-1].isdigit():
            return doc_id  # DA-027, SP-003, etc.
        return doc_id

    # ─── Implementación de la interfaz ────────────────────────────────────────

    def get_projects(self) -> List[Dict[str, Any]]:
        if not self._db:
            return [{"id": "mock-project-id", "name": "Proyecto Demo (Sin DB)"}]
        try:
            docs = self._db.collection("projects").limit(20).stream()
            return [{"id": p.id, "name": p.to_dict().get("name", p.id)} for p in docs]
        except Exception as e:
            logger.error(f"Error obteniendo proyectos: {e}")
            return [{"id": "mock-project-id", "name": "Proyecto Demo (Error)"}]

    def get_epics(self, project_id: str) -> List[Epic]:
        if not self._db:
            return []
        try:
            docs = self._tickets_ref(project_id).limit(TICKET_QUERY_LIMIT).stream()
            result = []
            for doc in docs:
                data = doc.to_dict()
                if data.get("type") in EPIC_TYPES:
                    data["id"] = doc.id
                    data["code"] = self._display_id(doc.id, data)
                    try:
                        result.append(Epic(**data))
                    except Exception as e:
                        logger.warning(f"Error parseando épica {doc.id}: {e}")
            return result
        except Exception as e:
            logger.error(f"Error obteniendo épicas: {e}")
            return []

    def get_stories(self, project_id: str) -> List[UserStory]:
        if not self._db:
            return []
        try:
            docs = self._tickets_ref(project_id).limit(TICKET_QUERY_LIMIT).stream()
            result = []
            for doc in docs:
                try:
                    data = doc.to_dict()
                    status = str(data.get("status", "")).lower()
                    if status not in DONE_STATUSES and data.get("type") in STORY_TYPES:
                        if not data.get("title"): data["title"] = "Sin título"
                        if not data.get("description"): data["description"] = ""
                        data["id"] = doc.id
                        data["code"] = self._display_id(doc.id, data)
                        result.append(UserStory(**data))
                except Exception as e:
                    logger.warning(f"Error parseando ticket {doc.id}: {e}")
            return result
        except Exception as e:
            logger.error(f"Error crítico obteniendo tickets: {e}")
            return []

    def save_ticket(self, project_id: str, ticket: Any) -> str:
        now = self._now_iso()
        if not ticket.createdAt:
            ticket.createdAt = now
        ticket.updatedAt = now

        if not self._db:
            import random
            logger.warning(f"Simulando guardado de '{ticket.title}'")
            return f"fake-id-{random.randint(1000, 9999)}"

        try:
            ticket_dict = ticket.model_dump(exclude_none=True, exclude={"id"})
            _, doc_ref = self._tickets_ref(project_id).add(ticket_dict)
            return doc_ref.id
        except Exception as e:
            logger.error(f"Error guardando ticket: {e}")
            raise

    def save_tickets_batch(self, project_id: str, tickets: list) -> List[str]:
        """Persiste múltiples tickets en paralelo."""
        ids = []
        with ThreadPoolExecutor(max_workers=MAX_PARALLEL_WORKERS) as executor:
            futures = {executor.submit(self.save_ticket, project_id, t): t for t in tickets}
            for future in as_completed(futures):
                try:
                    ids.append(future.result())
                except Exception as e:
                    logger.error(f"Error en guardado paralelo: {e}")
        return ids

    def update_ticket_score(self, project_id: str, ticket_id: str,
                            framework_field: str, score_data: Dict[str, Any]) -> None:
        if not self._db:
            return
        try:
            ref = self._tickets_ref(project_id).document(ticket_id)
            ref.update({framework_field: score_data, "updatedAt": self._now_iso()})
        except Exception as e:
            logger.error(f"Error actualizando {framework_field}: {e}")
            raise
