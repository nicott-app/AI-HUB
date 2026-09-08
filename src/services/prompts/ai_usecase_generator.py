"""
System Prompt y lógica de parseo para el Generador de Casos de Uso de IA.
"""
import json
import logging
from typing import List

from src.models.ai_usecase import AIUseCase
from src.config import LLM_TEMPERATURE_CREATIVE, LLM_MAX_TOKENS_PRIORITIZE

logger = logging.getLogger(__name__)

IMPACT_SCORE = {"Alto": 3, "Medio": 2, "Bajo": 1}
EFFORT_SCORE  = {"Alto": 1, "Medio": 2, "Bajo": 3}

SYSTEM_PROMPT = (
    "Eres un AI Strategy Consultant con 15 años de experiencia implementando proyectos de Inteligencia Artificial "
    "en empresas de todos los sectores. Tu tarea es analizar el contexto de una organización y generar una lista "
    "priorizada de casos de uso de IA que sean realistas, impactantes y accionables en el corto/medio plazo.\n\n"
    "Para cada caso de uso debes devolver un JSON con la clave 'use_cases' conteniendo una lista. "
    "Cada elemento DEBE seguir esta estructura exacta:\n"
    "{\n"
    "  \"title\": \"string — nombre claro y concreto del caso de uso\",\n"
    "  \"description\": \"string — descripción de qué problema resuelve y cómo lo hace la IA (2-3 frases)\",\n"
    "  \"business_area\": \"string — área de negocio (ej: Ventas, Operaciones, RRHH, Finanzas, Marketing, Customer Service)\",\n"
    "  \"ai_type\": \"string — tecnología de IA recomendada (ej: NLP / Chatbot, Computer Vision, Forecasting / Series Temporales, "
    "Clasificación ML, Automatización RPA + IA, Generative AI, Detección de Anomalías, Sistemas de Recomendación)\",\n"
    "  \"estimated_impact\": \"string — uno de: 'Alto', 'Medio', 'Bajo'\",\n"
    "  \"estimated_effort\": \"string — uno de: 'Alto', 'Medio', 'Bajo'\",\n"
    "  \"time_to_value\": \"string — tiempo estimado hasta ver resultados (ej: '1-2 meses', '3-6 meses', '6-12 meses')\",\n"
    "  \"kpis\": [\"string — KPI medible y específico que mejoraría este caso de uso\"],\n"
    "  \"prerequisites\": [\"string — prerequisito de datos, infraestructura o equipo necesario\"]\n"
    "}\n\n"
    "Reglas importantes:\n"
    "- Prioriza casos de uso con Quick Wins (alto impacto, bajo esfuerzo) para los primeros de la lista.\n"
    "- Sé específico y evita casos de uso genéricos como 'implementar un chatbot sin más contexto'.\n"
    "- Los KPIs deben ser medibles (con porcentajes, tiempos o cantidades).\n"
    "- Genera entre 5 y 8 casos de uso, ordenados de mayor a menor valor estratégico.\n"
    "- Responde siempre en el mismo idioma que el contexto del usuario."
)

CALL_PARAMS = {
    "temperature": LLM_TEMPERATURE_CREATIVE,
    "max_tokens": 900,
    "response_format": {"type": "json_object"},
}


def build_user_prompt(sector: str, company_size: str, pain_points: str, current_tech: str, goals: str) -> str:
    return (
        f"CONTEXTO DE LA ORGANIZACIÓN:\n"
        f"- Sector / Industria: {sector}\n"
        f"- Tamaño de la empresa: {company_size}\n"
        f"- Principales puntos de dolor o retos actuales: {pain_points}\n"
        f"- Tecnología / Infraestructura actual: {current_tech}\n"
        f"- Objetivos estratégicos del próximo año: {goals}\n\n"
        f"Por favor, genera una lista priorizada de casos de uso de IA para esta organización."
    )


def parse_response(content: str) -> List[AIUseCase]:
    """Parsea la respuesta JSON del LLM y calcula el score de priorización."""
    data = json.loads(content)
    use_cases = []
    for item in data.get("use_cases", []):
        # Calcular score = impacto / esfuerzo (más alto = mejor)
        impact = IMPACT_SCORE.get(item.get("estimated_impact", "Medio"), 2)
        effort = EFFORT_SCORE.get(item.get("estimated_effort", "Medio"), 2)
        item["priority_score"] = round((impact * effort) / 9 * 100, 1)  # Normalizado a 100
        try:
            use_cases.append(AIUseCase(**item))
        except Exception as e:
            logger.warning(f"Error parseando caso de uso: {e}")
    return sorted(use_cases, key=lambda x: x.priority_score or 0, reverse=True)
