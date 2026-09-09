"""
Caché compartido para todas las vistas de Streamlit.

Centralizar aquí el caché garantiza que las queries a Firebase se ejecuten
una sola vez, independientemente de cuántas vistas las consuman.

NOTA: cached_epics y cached_stories usan un patrón manual con st.session_state
en lugar de @st.cache_data porque los objetos Pydantic (Epic, UserStory) no son
serializables por el mecanismo interno de Streamlit.
"""
import time
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
    """Lista de proyectos cacheada 5 minutos. Los dicts son serializables sin problema."""
    return get_repository().get_projects()


def cached_epics(project_id: str):
    """Épicas de un proyecto cacheadas en session_state (compatible con objetos Pydantic)."""
    cache_key = f"_cache_epics_{project_id}"
    ts_key    = f"_cache_epics_ts_{project_id}"

    now = time.time()
    if cache_key not in st.session_state or (now - st.session_state.get(ts_key, 0)) > CACHE_TTL_SECONDS:
        st.session_state[cache_key] = get_repository().get_epics(project_id)
        st.session_state[ts_key]    = now

    return st.session_state[cache_key]


def cached_stories(project_id: str):
    """Tickets priorizables de un proyecto cacheados en session_state (compatible con objetos Pydantic)."""
    cache_key = f"_cache_stories_{project_id}"
    ts_key    = f"_cache_stories_ts_{project_id}"

    now = time.time()
    if cache_key not in st.session_state or (now - st.session_state.get(ts_key, 0)) > CACHE_TTL_SECONDS:
        st.session_state[cache_key] = get_repository().get_stories(project_id)
        st.session_state[ts_key]    = now

    return st.session_state[cache_key]

