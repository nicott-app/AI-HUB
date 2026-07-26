import os
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore import Client
from typing import List, Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

from src.models.agile import UserStory, Epic

logger = logging.getLogger(__name__)

class FirebaseClient:
    """Cliente Singleton para la conexión con Firebase Admin."""
    _instance = None
    _db: Client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FirebaseClient, cls).__new__(cls)
            cls._instance._initialize_firebase()
        return cls._instance

    def _initialize_firebase(self) -> None:
        """Inicializa la conexión con Firebase si no se ha hecho ya."""
        if not firebase_admin._apps:
            cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH", "./firebase-credentials.json")
            try:
                if not os.path.exists(cred_path):
                    # Usaremos credenciales por defecto de GCP si no hay archivo
                    cred = credentials.ApplicationDefault()
                    firebase_admin.initialize_app(cred)
                else:
                    cred = credentials.Certificate(cred_path)
                    firebase_admin.initialize_app(cred)
                
                self._db = firestore.client()
                logger.info("Firebase inicializado correctamente.")
            except Exception as e:
                logger.error(f"No se pudo cargar credenciales de Firebase. {e}")
        else:
            if self._db is None:
                self._db = firestore.client()

    def get_epic(self, project_id: str, epic_id: str) -> Optional[Epic]:
        """Obtiene una épica desde Firebase en el proyecto especificado."""
        if not self._db: 
            logger.warning("Simulando get_epic por falta de BD.")
            return None
            
        try:
            doc_ref = self._db.collection("projects").document(project_id).collection("tickets").document(epic_id)
            doc = doc_ref.get()
            if doc.exists:
                data = doc.to_dict()
                data["id"] = doc.id
                return Epic(**data)
        except Exception as e:
            logger.error(f"Error obteniendo épica {epic_id}: {e}")
        return None

    def save_user_story(self, project_id: str, story: UserStory) -> str:
        """Guarda una historia de usuario en Firebase y retorna su ID."""
        return self.save_ticket(project_id, story)

    def save_ticket(self, project_id: str, ticket: Any) -> str:
        """Guarda un ticket en Firebase y retorna su ID, inyectando fechas ISO 8601."""
        from datetime import datetime, timezone
        now_iso = datetime.now(timezone.utc).isoformat()
        if not ticket.createdAt:
            ticket.createdAt = now_iso
        ticket.updatedAt = now_iso

        if not self._db: 
            logger.warning(f"Simulando guardado de ticket '{ticket.title}' por falta de BD.")
            import random
            return f"fake-id-{random.randint(1000, 9999)}"
            
        try:
            tickets_ref = self._db.collection("projects").document(project_id).collection("tickets")
            ticket_dict = ticket.model_dump(exclude_none=True, exclude={"id"})
            _, doc_ref = tickets_ref.add(ticket_dict)
            return doc_ref.id
        except Exception as e:
            logger.error(f"Error guardando ticket: {e}")
            raise

    def save_tickets_batch(self, project_id: str, tickets: list) -> list:
        """Guarda múltiples tickets en paralelo usando ThreadPoolExecutor. Mucho más rápido que secuencial."""
        ids = []
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = {executor.submit(self.save_ticket, project_id, t): t for t in tickets}
            for future in as_completed(futures):
                try:
                    ids.append(future.result())
                except Exception as e:
                    logger.error(f"Error en guardado paralelo: {e}")
        return ids

    def update_ticket_score(self, project_id: str, ticket_id: str, framework_field: str, score_data: Dict[str, Any]) -> None:
        if not self._db: return
        try:
            from datetime import datetime, timezone
            doc_ref = self._db.collection("projects").document(project_id).collection("tickets").document(ticket_id)
            doc_ref.update({framework_field: score_data, "updatedAt": datetime.now(timezone.utc).isoformat()})
        except Exception as e:
            logger.error(f"Error actualizando {framework_field}: {e}")
            raise

    def get_epics(self, project_id: str) -> List[Epic]:
        """Obtiene tickets de tipo análisis o desarrollo (tratados como épicas)."""
        if not self._db: return []
        try:
            tickets_ref = self._db.collection("projects").document(project_id).collection("tickets")
            # Filtrado en Python para evitar problemas de índices complejos en Firestore si no están creados
            docs = tickets_ref.limit(50).stream()
            result = []
            for doc in docs:
                data = doc.to_dict()
                if data.get("type") in ["analisis", "desarrollo"]:
                    data["id"] = doc.id
                    result.append(Epic(**data))
            return result
        except Exception as e:
            logger.error(f"Error obteniendo epics: {e}")
            return []

    def get_user_stories(self, project_id: str) -> List[UserStory]:
        """Obtiene tickets para priorizar (tarea, mejora, desarrollo, entregable)."""
        if not self._db: return []
        try:
            tickets_ref = self._db.collection("projects").document(project_id).collection("tickets")
            docs = tickets_ref.limit(200).stream()  # Aumentado para soportar proyectos grandes
            result = []
            for doc in docs:
                try:
                    data = doc.to_dict()
                    status = str(data.get("status", "")).lower()
                    
                    if status != "done":
                        if data.get("type") in ["tarea", "mejora", "desarrollo", "entregable"]:
                            # Asegurar campos obligatorios para Pydantic si vienen nulos de DB
                            if not data.get("title"): data["title"] = "Sin título"
                            if not data.get("description"): data["description"] = ""
                            data["id"] = doc.id
                            result.append(UserStory(**data))
                except Exception as doc_e:
                    logger.warning(f"Error parseando ticket {doc.id}: {doc_e}")
                    
            return result
        except Exception as e:
            logger.error(f"Error crítico obteniendo stories: {e}")
            return []

    def get_projects(self) -> List[Dict[str, Any]]:
        """Obtiene la lista de proyectos disponibles (solo para la UI)."""
        if not self._db: 
            return [{"id": "mock-project-id", "name": "Proyecto Demo (Sin DB)"}]
            
        try:
            projects = self._db.collection("projects").limit(20).stream()
            result = []
            for p in projects:
                data = p.to_dict()
                result.append({"id": p.id, "name": data.get("name", p.id)})
            return result
        except Exception as e:
            logger.error(f"Error obteniendo proyectos: {e}")
            return [{"id": "mock-project-id", "name": "Proyecto Demo (Error)"}]
