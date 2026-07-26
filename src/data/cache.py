"""
Caché compartido para todas las vistas de Streamlit.

Centralizar aquí el caché garantiza que las queries a Firebase se ejecuten
una sola vez, independientemente de cuántas vistas las consuman.
"""
import streamlit as st
from src.config import CACHE_TTL_SECONDS


@st.cache_resource
def get_repository():
    """Singleton del repositorio de tickets. Solo se instancia una vez por sesión."""
    from src.repositories.firebase_repository import FirebaseRepository
    return FirebaseRepository()


@st.cache_resource
def get_llm_service():
    """Singleton del servicio LLM. Solo se instancia una vez por sesión."""
    from src.services.llm_service import LLMService
    return LLMService()


@st.cache_data(ttl=CACHE_TTL_SECONDS, show_spinner=False)
def cached_projects():
    """Lista de proyectos cacheada 5 minutos."""
    return get_repository().get_projects()


@st.cache_data(ttl=CACHE_TTL_SECONDS, show_spinner=False)
def cached_epics(project_id: str):
    """Épicas de un proyecto cacheadas 5 minutos."""
    return get_repository().get_epics(project_id)


@st.cache_data(ttl=CACHE_TTL_SECONDS, show_spinner=False)
def cached_stories(project_id: str):
    """Tickets priorizables de un proyecto cacheados 5 minutos."""
    return get_repository().get_stories(project_id)
