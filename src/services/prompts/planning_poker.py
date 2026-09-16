PLANNING_POKER_SYSTEM_PROMPT = """
Eres un experimentado Agile Coach y Tech Lead. 
Tu objetivo es estimar el esfuerzo y complejidad de una serie de Historias de Usuario utilizando la técnica de Planning Poker.
Debes usar estrictamente la serie de Fibonacci para los Puntos de Historia (Story Points): 1, 2, 3, 5, 8, 13, 21.

Para estimar, considera los siguientes factores (Complexity Drivers):
- Deuda técnica e integraciones con terceros.
- Nivel de detalle de los Criterios de Aceptación.
- Riesgo asociado o dependencias ocultas.
- Esfuerzo de QA (Pruebas).

Además de los Story Points, debes proveer una conversión MUY aproximada en `estimated_hours`. (Por ejemplo, usa tu propio criterio heurístico para asignar horas lógicas, típicamente entre 4h y 8h por Story Point).

Debes devolver UNICAMENTE un array de objetos JSON válido con la siguiente estructura (uno por cada historia evaluada en el mismo orden):

[
  {
    "story_points": int,
    "estimated_hours": int,
    "rationale": "Justificación clara y concisa de por qué se asignó esta puntuación. Menciona los factores que más influyen.",
    "risks": ["Riesgo 1", "Riesgo 2"],
    "complexity_drivers": ["Integración externa", "Falta de definición clara"]
  }
]

IMPORTANTE: El JSON debe estar perfectamente formateado sin texto adicional. Debe ser un array `[...]`.
"""

def build_planning_poker_prompt(stories: list) -> str:
    prompt = "Estima el esfuerzo para las siguientes historias de usuario. Debes devolver un array JSON con la misma cantidad de elementos.\n\n"
    for i, story in enumerate(stories):
        prompt += f"Historia {i}:\n"
        prompt += f"Título: {story.title}\n"
        prompt += f"Descripción: {story.description}\n"
        if story.acceptanceCriteria:
            prompt += f"Criterios de Aceptación: {story.acceptanceCriteria}\n"
        prompt += "---\n"
    return prompt

CALL_PARAMS = {
    "temperature": 0.3,
    "max_tokens": 1500,
    "response_format": {"type": "json_object"}
}

def parse_response(content: str) -> list:
    import json
    import logging
    from src.models.scores import PlanningPokerEstimation
    
    logger = logging.getLogger(__name__)
    
    try:
        data = json.loads(content)
        # Algunos LLM devuelven un objeto raíz si forzamos json_object
        if isinstance(data, dict):
            # Buscar el primer valor que sea una lista
            for v in data.values():
                if isinstance(v, list):
                    data = v
                    break
            else:
                data = [data] # Fallback
                
        estimations = []
        for item in data:
            est = PlanningPokerEstimation(**item)
            estimations.append(est)
        return estimations
    except Exception as e:
        logger.error(f"Error parseando Planning Poker: {e}")
        return []
