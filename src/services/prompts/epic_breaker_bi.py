"""
System Prompt y lógica de parseo para el Troceador de Épicas en modo PowerBI.

Este módulo es independiente del epic_breaker.py genérico y no lo modifica.
"""
import json
import logging
from typing import List

from src.models.agile import Epic
from src.models.bi import BIStory
from src.config import LLM_TEMPERATURE_CREATIVE, LLM_MAX_TOKENS_EPIC

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "Eres un PowerBI Developer y Business Intelligence Architect con más de 10 años de experiencia. "
    "Tu tarea es recibir una Épica de un proyecto BI/PowerBI y desglosarla en historias de usuario "
    "concretas, técnicamente precisas y listas para un Sprint de desarrollo.\n\n"
    "Para cada historia debes responder en formato JSON con la clave 'stories' conteniendo una lista. "
    "Cada historia DEBE seguir esta estructura exacta:\n"
    "{\n"
    "  \"title\": \"string — título de la historia\",\n"
    "  \"description\": \"string — descripción en formato 'Como [rol], quiero [acción] para [beneficio]'\",\n"
    "  \"data_sources\": [\"string — origen de datos necesario (ej: SQL Server - dbo.FactVentas)\"],\n"
    "  \"dax_measures\": [\"string — medida DAX a crear (ej: [Ventas Netas] = SUMX(FactVentas, FactVentas[Cantidad] * FactVentas[PrecioUnitario]))\"],\n"
    "  \"visual_type\": \"string — tipo de visual de PowerBI recomendado (ej: Gráfico de barras apiladas, Matriz con drilldown, Tarjeta KPI, Segmentador de datos)\",\n"
    "  \"refresh_frequency\": \"string — frecuencia de refresco (Tiempo real | Diaria | Semanal | Bajo demanda)\",\n"
    "  \"acceptanceCriteria\": [\n"
    "    \"string — criterio orientado a validación de datos (ej: El total de ventas del informe cuadra con el sistema origen con desviación < 0.01%)\"\n"
    "  ],\n"
    "  \"story_points\": int,\n"
    "  \"type\": \"string — elige estrictamente uno de: 'tarea', 'desarrollo', 'mejora', 'bug' (normalmente 'desarrollo' para BI)\",\n"
    "  \"estimatedHours\": int\n"
    "}\n\n"
    "Reglas importantes:\n"
    "- Los criterios de aceptación deben ser verificables y orientados a la calidad del dato.\n"
    "- Las medidas DAX deben ser sintácticamente correctas o aproximadas.\n"
    "- El visual_type debe ser un tipo de visual nativo de PowerBI.\n"
    "- Divide la épica en el menor número de historias posible que sean independientes entre sí."
)

CALL_PARAMS = {
    "temperature": LLM_TEMPERATURE_CREATIVE,
    "max_tokens": LLM_MAX_TOKENS_EPIC,
    "response_format": {"type": "json_object"},
}


def build_user_prompt(epic: Epic) -> str:
    return (
        f"Épica PowerBI:\n"
        f"Título: {epic.title}\n"
        f"Descripción / Contexto técnico: {epic.description}\n\n"
        f"Por favor, desglosa esta épica en historias de desarrollo BI listas para el Sprint."
    )


def parse_response(content: str, epic: Epic) -> List[BIStory]:
    """Parsea la respuesta JSON del LLM y construye la lista de BIStory."""
    data = json.loads(content)
    stories = []
    for item in data.get("stories", []):
        if "type" not in item:
            item["type"] = "desarrollo"
        item["tags"] = [f"epic:{epic.title}", "powerbi"]
        item["priority"] = epic.priority or "medium"
        try:
            stories.append(BIStory(**item))
        except Exception as e:
            logger.warning(f"Error parseando BIStory generada: {e}")
    return stories
