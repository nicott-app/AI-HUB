SYSTEM_PROMPT = """
Eres un experimentado Agile Coach y Delivery Manager.
Se te proporcionarán las métricas cuantitativas actuales del tablero Kanban de un proyecto (WIP, cantidad de historias, puntos estimados, tickets bloqueados, distribución por estado).

Tu objetivo es redactar un diagnóstico cualitativo profundo sobre la salud del proyecto. No te limites a repetir los números; interpreta lo que significan para el flujo de valor.

Reglas:
1. Detecta posibles cuellos de botella (por ejemplo, si hay demasiados tickets en QA comparado con los tickets en Progreso).
2. Advierte sobre bloqueos críticos.
3. Clasifica el estado general como "Saludable", "En Riesgo", o "Crítico".
4. Da recomendaciones procesables para el equipo.

Debes devolver UNICAMENTE un objeto JSON válido con la siguiente estructura:
{
  "overall_status": "Saludable | En Riesgo | Crítico",
  "summary": "Resumen claro y conciso del diagnóstico del flujo de trabajo.",
  "bottlenecks": ["Cuello de botella 1", "Cuello de botella 2"],
  "recommendations": ["Recomendación 1", "Recomendación 2"]
}
"""

def build_user_prompt(metrics: dict) -> str:
    prompt = "Métricas actuales del proyecto:\n\n"
    for key, value in metrics.items():
        prompt += f"- {key}: {value}\n"
    return prompt

CALL_PARAMS = {
    "temperature": 0.2,
    "max_tokens": 1500,
    "response_format": {"type": "json_object"}
}

def parse_response(content: str):
    import json
    import logging
    from src.models.health import SprintHealthDiagnosis
    
    logger = logging.getLogger(__name__)
    
    try:
        data = json.loads(content)
        # Algunos modelos envuelven en root object
        if "overall_status" not in data:
            for v in data.values():
                if isinstance(v, dict) and "overall_status" in v:
                    data = v
                    break
        return SprintHealthDiagnosis(**data)
    except Exception as e:
        logger.error(f"Error parseando Health Diagnosis: {e}")
        return SprintHealthDiagnosis(
            overall_status="Desconocido",
            summary="Ocurrió un error interpretando los datos.",
            bottlenecks=[],
            recommendations=[]
        )
