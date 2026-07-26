"""System Prompt y lógica de parseo para el Troceador de Épicas."""
import json
import logging
from typing import List

from src.models.agile import Epic, UserStory
from src.config import LLM_TEMPERATURE_CREATIVE, LLM_MAX_TOKENS_EPIC

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "Eres un Agile Product Manager experto. Tu tarea es recibir una Épica "
    "y desglosarla en historias de usuario pequeñas, independientes y valiosas.\n"
    "Debes responder en formato JSON, devolviendo un objeto con la clave 'stories' "
    "que contenga una lista de historias. Cada historia debe tener esta estructura exacta:\n"
    "{\n"
    "  \"title\": \"string\",\n"
    "  \"description\": \"string\",\n"
    "  \"acceptanceCriteria\": [\"string\", \"string\"],\n"
    "  \"story_points\": int\n"
    "}\n"
)

CALL_PARAMS = {
    "temperature": LLM_TEMPERATURE_CREATIVE,
    "max_tokens": LLM_MAX_TOKENS_EPIC,
    "response_format": {"type": "json_object"},
}


def build_user_prompt(epic: Epic) -> str:
    return (
        f"Épica Título: {epic.title}\n"
        f"Épica Descripción: {epic.description}\n"
        f"Por favor, desglosa esta épica."
    )


def parse_response(content: str, epic: Epic) -> List[UserStory]:
    """Parsea la respuesta JSON del LLM y construye la lista de UserStory."""
    data = json.loads(content)
    stories = []
    for item in data.get("stories", []):
        item["type"] = "tarea"
        item["tags"] = [f"epic:{epic.title}"]
        item["priority"] = epic.priority or "medium"
        try:
            stories.append(UserStory(**item))
        except Exception as e:
            logger.warning(f"Error parseando historia generada: {e}")
    return stories
