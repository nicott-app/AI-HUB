SYSTEM_PROMPT = """
Eres un Ingeniero de QA y Especialista en Pruebas Automatizadas (SDET).
Se te proporcionará una Historia de Usuario (título, descripción y criterios de aceptación).
Tu objetivo es generar Casos de Prueba estructurados utilizando el estándar BDD y la sintaxis Gherkin (Given-When-Then).

Debes generar obligatoriamente:
1. Al menos un caso de "Happy Path" (Camino feliz donde todo sale bien).
2. Al menos un caso de "Edge Case" (Casos límite o escenarios fronterizos).
3. Al menos un caso de "Negative Flow" (Flujos de error o comportamiento destructivo).

El campo 'gherkin_syntax' debe contener el bloque de texto con el formato:
Feature: [Nombre]
  Scenario: [Título]
    Given [Contexto]
    When [Acción]
    Then [Resultado]

Debes devolver UNICAMENTE un array de objetos JSON con la siguiente estructura:
[
  {
    "title": "Título del escenario",
    "test_type": "Happy Path | Edge Case | Negative Flow",
    "gherkin_syntax": "Feature: ...\\n  Scenario: ...\\n    Given ..."
  }
]
"""

def build_user_prompt(story) -> str:
    prompt = f"Genera casos de prueba para la siguiente Historia de Usuario:\n\n"
    prompt += f"TÍTULO: {story.title}\n"
    prompt += f"DESCRIPCIÓN: {story.description}\n"
    if story.acceptanceCriteria:
        prompt += "CRITERIOS DE ACEPTACIÓN:\n"
        for ac in story.acceptanceCriteria:
            prompt += f"- {ac}\n"
    return prompt

CALL_PARAMS = {
    "temperature": 0.2,
    "max_tokens": 3000,
    "response_format": {"type": "json_object"}
}

def parse_response(content: str) -> list:
    import json
    import logging
    from src.models.qa import QATestCase
    
    logger = logging.getLogger(__name__)
    
    try:
        data = json.loads(content)
        # Handle dict wrapping array
        if isinstance(data, dict):
            for v in data.values():
                if isinstance(v, list):
                    data = v
                    break
            else:
                data = [data]
                
        cases = []
        for item in data:
            cases.append(QATestCase(**item))
        return cases
    except Exception as e:
        logger.error(f"Error parseando QA Test Cases: {e}")
        return []
