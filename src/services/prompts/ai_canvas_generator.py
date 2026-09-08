"""
System Prompt y lógica de parseo para el Canvas de Proyecto IA.
"""
import json
import logging
from typing import Optional

from src.models.ai_canvas import AIProjectCanvas
from src.config import LLM_TEMPERATURE_ANALYTICAL, LLM_MAX_TOKENS_PRIORITIZE

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "Eres un AI Project Manager y consultor experto en implementación de proyectos de Inteligencia Artificial. "
    "Tu tarea es recibir la descripción inicial de un proyecto de IA y generar un Canvas de Proyecto completo, "
    "riguroso y listo para presentar a stakeholders.\n\n"
    "Debes responder ÚNICAMENTE con un objeto JSON que siga esta estructura exacta:\n"
    "{\n"
    "  \"problem_statement\": \"string — 2-3 frases que describan el problema de negocio con precisión\",\n"
    "  \"affected_users\": \"string — qué roles o departamentos están afectados\",\n"
    "  \"current_pain\": \"string — impacto medible del problema hoy (tiempo, coste, riesgo)\",\n"
    "  \"proposed_solution\": \"string — descripción clara de la solución de IA propuesta\",\n"
    "  \"ai_approach\": \"string — tecnología/enfoque de IA recomendado y por qué\",\n"
    "  \"alternatives_considered\": [\"string — alternativa no-IA y por qué se descarta\"],\n"
    "  \"data_sources\": [\"string — fuente de datos, formato y estado de disponibilidad\"],\n"
    "  \"data_volume\": \"string — estimación del volumen de datos\",\n"
    "  \"data_quality_risks\": [\"string — riesgo de calidad o acceso a datos\"],\n"
    "  \"primary_kpi\": \"string — KPI principal medible\",\n"
    "  \"secondary_kpis\": [\"string — KPI secundario\"],\n"
    "  \"baseline\": \"string — situación actual medible\",\n"
    "  \"target\": \"string — objetivo cuantificado a lograr\",\n"
    "  \"team_needed\": [\"string — rol necesario y responsabilidad\"],\n"
    "  \"infrastructure\": \"string — infraestructura requerida\",\n"
    "  \"estimated_budget\": \"string — rango de inversión estimada\",\n"
    "  \"risks\": [\n"
    "    {\"risk\": \"string\", \"probability\": \"Alta/Media/Baja\", \"impact\": \"Alto/Medio/Bajo\", \"mitigation\": \"string\"}\n"
    "  ],\n"
    "  \"phases\": [\n"
    "    {\"name\": \"string\", \"duration\": \"string\", \"deliverables\": [\"string\"]}\n"
    "  ],\n"
    "  \"total_duration\": \"string — duración total del proyecto\",\n"
    "  \"business_value\": \"string — valor estratégico para la organización\",\n"
    "  \"roi_estimate\": \"string — ROI estimado, cuantitativo o cualitativo\"\n"
    "}\n\n"
    "Reglas:\n"
    "- Sé específico, pragmático y realista. Evita generalidades.\n"
    "- Los KPIs deben ser medibles con números concretos.\n"
    "- Las fases deben ser secuenciales y tener nombre (ej: 'Fase 1: Discovery y datos').\n"
    "- El roadmap debe contemplar como mínimo: Discovery, Prototipo/PoC, Piloto y Producción.\n"
    "- Responde en el mismo idioma que el usuario.\n"
    "- Responde SOLO con el JSON, sin texto adicional."
)

CALL_PARAMS = {
    "temperature": LLM_TEMPERATURE_ANALYTICAL,
    "max_tokens": LLM_MAX_TOKENS_PRIORITIZE,
    "response_format": {"type": "json_object"},
}


def build_user_prompt(
    project_name: str,
    objective: str,
    sector: str,
    context: str,
    constraints: str,
) -> str:
    return (
        f"INFORMACIÓN DEL PROYECTO:\n"
        f"- Nombre del proyecto: {project_name}\n"
        f"- Objetivo principal: {objective}\n"
        f"- Sector / contexto de la empresa: {sector}\n"
        f"- Información adicional / contexto técnico: {context}\n"
        f"- Restricciones conocidas (tiempo, presupuesto, tecnología): {constraints}\n\n"
        f"Genera el Canvas de Proyecto IA completo para este proyecto."
    )


def parse_response(content: str) -> Optional[AIProjectCanvas]:
    """Parsea la respuesta JSON del LLM y construye el AIProjectCanvas."""
    # Qwen a veces encierra el JSON en un bloque ```json ... ```, lo limpiamos
    cleaned = content.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("```")[1]
        if cleaned.startswith("json"):
            cleaned = cleaned[4:]
    cleaned = cleaned.strip()
    data = json.loads(cleaned)
    return AIProjectCanvas(**data)
