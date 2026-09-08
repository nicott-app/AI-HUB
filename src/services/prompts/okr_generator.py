import json
from typing import Optional
from src.models.okr import OKRSet

SYSTEM_PROMPT = """Eres un Agile Strategy Coach experto en el framework OKR (Objectives and Key Results).
Tu tarea es traducir el contexto y las prioridades estratégicas del usuario en un conjunto formal de OKRs estructurados en JSON.

REGLAS ESTRICTAS PARA OKRs:
1. OBJECTIVES (O): Deben ser CUALITATIVOS, inspiradores, memorables y ambiciosos. NUNCA incluyas números en el título de un Objective.
2. KEY RESULTS (KRs): Deben ser CUANTITATIVOS y estrictamente medibles. No uses KRs booleanos (hecho/no hecho).
   - Debes proveer un "baseline" (valor inicial/actual) y un "target" (valor meta). Ambos deben ser numéricos (float o int).
   - Especifica la unidad (ej. "%", "USD", "MAU", "segundos").
3. INICIATIVAS: Para cada KR, sugiere 2 a 3 iniciativas o épicas de alto nivel que ayudarán a mover la aguja de esa métrica.

FORMATO DE SALIDA:
Devuelve ÚNICAMENTE un JSON válido que coincida exactamente con esta estructura, sin texto adicional antes ni después:
{
  "timeframe": "Ciclo temporal (ej. Q3 2026)",
  "strategic_alignment": "Cómo esto empuja la visión a largo plazo",
  "objectives": [
    {
      "title": "Conquistar el mercado corporativo (¡Sin números!)",
      "description": "Justificación de la importancia...",
      "key_results": [
        {
          "title": "Aumentar la conversión de leads B2B",
          "metric_name": "Conversión B2B",
          "baseline": 12.5,
          "target": 25.0,
          "unit": "%",
          "initiatives": ["Rediseñar landing B2B", "Lanzar campaña de retargeting LinkedIn"]
        }
      ]
    }
  ]
}
"""

CALL_PARAMS = {
    "temperature": 0.3,  # Baja temperatura para asegurar estructura JSON estricta y analítica
    "max_tokens": 2048,
    "response_format": {"type": "json_object"}
}

def build_user_prompt(project_context: str, timeframe: str, strategic_focus: str) -> str:
    return f"""Por favor, genera un set de OKRs (2 a 4 Objetivos, con 3-5 KRs cada uno).

Contexto del Producto/Organización:
{project_context}

Ciclo temporal objetivo:
{timeframe}

Foco Estratégico o Reto Principal:
{strategic_focus}

Asegúrate de que los KRs sean métricas reales, desafiantes pero alcanzables, y propón iniciativas que tengan sentido para el contexto dado.
"""

def parse_response(response_content: str) -> Optional[OKRSet]:
    try:
        # Limpiar posibles bloques markdown de código si el modelo ignora el response_format
        clean_content = response_content.strip()
        if clean_content.startswith("```json"):
            clean_content = clean_content[7:]
        if clean_content.endswith("```"):
            clean_content = clean_content[:-3]
        
        data = json.loads(clean_content)
        return OKRSet(**data)
    except Exception as e:
        print(f"Error parseando OKRSet: {e}\nContenido recibido: {response_content}")
        return None
