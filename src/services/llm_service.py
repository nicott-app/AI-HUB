"""
LLMService — Capa HTTP fina hacia la API de Groq.

Esta clase solo gestiona la comunicación con Groq. Toda la lógica de
prompts, parseo y ordenación está delegada a src/services/prompts/.
Esto permite cambiar el proveedor de LLM (OpenAI, Gemini, Ollama...)
modificando únicamente este fichero.
"""
import logging
from typing import List

from groq import Groq

from src.config import LLM_MODEL
from src.models.agile import Epic, UserStory, PrioritizedStory
from src.models.bi import BIStory
from src.services.prompts import epic_breaker, epic_breaker_bi, prioritizer

logger = logging.getLogger(__name__)


class LLMService:
    def __init__(self):
        import os
        
        # 1. Intentar variable de entorno local (.env)
        self.api_key = os.getenv("GROQ_API_KEY")
        
        # 2. Intentar Streamlit Secrets si está en la nube
        if not self.api_key:
            try:
                import streamlit as st
                self.api_key = st.secrets.get("GROQ_API_KEY")
            except Exception:
                pass
                
        if not self.api_key:
            logger.warning("GROQ_API_KEY no encontrada. Configúrala en Streamlit Secrets.")
            self.api_key = "MISSING_API_KEY" # Para evitar TypeError en Groq()
            
        self.client = Groq(api_key=self.api_key)
        self.model = LLM_MODEL

    def _call(self, system_prompt: str, user_content: str, **params) -> str:
        """Realiza la llamada HTTP a Groq y devuelve el contenido crudo."""
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            model=self.model,
            **params,
        )
        return response.choices[0].message.content

    def break_epic_into_stories(self, epic: Epic) -> List[UserStory]:
        """Desglosa una épica en historias de usuario usando el LLM."""
        try:
            content = self._call(
                system_prompt=epic_breaker.SYSTEM_PROMPT,
                user_content=epic_breaker.build_user_prompt(epic),
                **epic_breaker.CALL_PARAMS,
            )
            return epic_breaker.parse_response(content, epic)
        except Exception as e:
            logger.error(f"Error en break_epic_into_stories: {e}")
            raise

    def break_epic_into_bi_stories(self, epic: Epic) -> List[BIStory]:
        """Desglosa una épica en historias de desarrollo PowerBI/BI usando el LLM.
        
        Genera historias enriquecidas con orígenes de datos, medidas DAX,
        tipo de visual y frecuencia de refresco.
        """
        try:
            content = self._call(
                system_prompt=epic_breaker_bi.SYSTEM_PROMPT,
                user_content=epic_breaker_bi.build_user_prompt(epic),
                **epic_breaker_bi.CALL_PARAMS,
            )
            return epic_breaker_bi.parse_response(content, epic)
        except Exception as e:
            logger.error(f"Error en break_epic_into_bi_stories: {e}")
            raise

    def prioritize_stories(self, stories: List[UserStory], framework: str) -> List[PrioritizedStory]:
        """Prioriza una lista de historias con el framework indicado."""
        if not stories:
            return []

        system_prompt = prioritizer.SYSTEM_PROMPTS.get(framework)
        if not system_prompt:
            raise ValueError(f"Framework no soportado: {framework}")

        try:
            content = self._call(
                system_prompt=system_prompt,
                user_content=prioritizer.build_payload(stories),
                **prioritizer.CALL_PARAMS,
            )
            return prioritizer.parse_and_sort(content, stories, framework)
        except Exception as e:
            logger.error(f"Error en prioritize_stories ({framework}): {e}")
            raise
