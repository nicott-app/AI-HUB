SYSTEM_PROMPT = """
Eres un Technical Writer y Product Manager experto.
Tu objetivo es leer una lista de Historias de Usuario completadas durante un Sprint o ciclo de desarrollo y redactar unas Notas de la Versión (Release Notes) profesionales.

Se te proporcionará:
- VERSIÓN: El número de versión (ej. v1.2.0).
- TONO: "business" (para clientes/marketing) o "technical" (para el equipo técnico interno).
- HISTORIAS: La lista de tareas completadas (con sus títulos, descripciones y tipos).

Instrucciones:
1. Agrupa los cambios lógicamente (Nuevas Funcionalidades, Mejoras, Correcciones).
2. Si el TONO es "business":
   - Usa un lenguaje enfocado en los beneficios para el cliente.
   - Omite jerga técnica profunda (bases de datos, migraciones, refactors).
   - Usa un estilo de marketing amigable.
3. Si el TONO es "technical":
   - Sé preciso y detallado.
   - Incluye menciones a arquitectura, refactors, y detalles de bajo nivel presentes en las historias.
4. Genera el documento final en un formato Markdown impecable en el campo 'markdown_content'.

Debes devolver UNICAMENTE un objeto JSON válido con la siguiente estructura:
{
  "version": "v1.2.0",
  "summary": "Resumen general de 2-3 líneas",
  "features": ["Feature destacada 1", "Feature destacada 2"],
  "technical_details": ["Detalle técnico 1", "Bugfix 1"],
  "markdown_content": "# Release Notes v1.2.0\\n\\n## Novedades..."
}
"""

def build_user_prompt(stories: list, version: str, tone: str) -> str:
    prompt = f"VERSIÓN: {version}\n"
    prompt += f"TONO: {tone}\n\n"
    prompt += "HISTORIAS COMPLETADAS:\n"
    for i, s in enumerate(stories):
        prompt += f"\n--- Tarea {i+1} ---\n"
        prompt += f"Código: {s.code}\n"
        prompt += f"Título: {s.title}\n"
        if s.type:
            prompt += f"Tipo: {s.type}\n"
        if s.description:
            prompt += f"Descripción: {s.description}\n"
    return prompt

CALL_PARAMS = {
    "temperature": 0.4,
    "max_tokens": 4000,
    "response_format": {"type": "json_object"}
}

def parse_response(content: str):
    import json
    import logging
    from src.models.docs import ReleaseNotes
    
    logger = logging.getLogger(__name__)
    
    try:
        data = json.loads(content)
        # Algunos modelos envuelven en root object
        if "markdown_content" not in data:
            for v in data.values():
                if isinstance(v, dict) and "markdown_content" in v:
                    data = v
                    break
        return ReleaseNotes(**data)
    except Exception as e:
        logger.error(f"Error parseando Release Notes: {e}")
        return None
