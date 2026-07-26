"""System Prompts y lógica de parseo para todos los frameworks de priorización."""
import json
import logging
from typing import List

from src.models.agile import UserStory, PrioritizedStory
from src.models.scores import RICEScore, WSJFScore, MoSCoWScore, KanoScore, ValueComplexityScore
from src.config import LLM_TEMPERATURE_ANALYTICAL, LLM_MAX_TOKENS_PRIORITIZE

logger = logging.getLogger(__name__)

# ─── System Prompts por framework ─────────────────────────────────────────────
SYSTEM_PROMPTS: dict = {
    "RICE": (
        "Eres un Agile Product Manager experto.\n"
        "Evalúa las Historias (JSON) usando RICE:\n"
        "- Reach: (ej. 10 a 1000).\n"
        "- Impact: 3, 2, 1, 0.5, 0.25.\n"
        "- Confidence: 100, 80 o 50.\n"
        "- Effort: (mínimo 0.5).\n"
        "Devuelve JSON con 'results' (lista de {'id', 'score': {'reach': float, 'impact': float, "
        "'confidence': float, 'effort': float, 'total_score': float, 'rationale': 'str'}})\n"
        "total_score = (Reach * Impact * Confidence) / Effort."
    ),
    "WSJF": (
        "Eres un Agile Product Manager experto en SAFe.\n"
        "Evalúa las Historias (JSON) usando WSJF (Weighted Shortest Job First):\n"
        "- user_business_value: 1 a 20.\n"
        "- time_criticality: 1 a 20.\n"
        "- risk_reduction_opportunity: 1 a 20.\n"
        "- job_size: 1 a 20.\n"
        "Devuelve JSON con 'results' (lista de {'id', 'score': {'user_business_value': float, "
        "'time_criticality': float, 'risk_reduction_opportunity': float, 'job_size': float, "
        "'total_score': float, 'rationale': 'str'}})\n"
        "total_score = (user_business_value + time_criticality + risk_reduction_opportunity) / job_size."
    ),
    "MoSCoW": (
        "Eres un Agile Product Manager experto.\n"
        "Evalúa las Historias (JSON) usando MoSCoW.\n"
        "Devuelve JSON con 'results' (lista de {'id', 'score': {'category': 'str', 'rationale': 'str'}})\n"
        "Categorías válidas exactas: 'Must Have', 'Should Have', 'Could Have', 'Won\\'t Have'."
    ),
    "Kano": (
        "Eres un Agile Product Manager experto.\n"
        "Evalúa las Historias (JSON) usando el Modelo Kano.\n"
        "Devuelve JSON con 'results' (lista de {'id', 'score': {'category': 'str', 'rationale': 'str'}})\n"
        "Categorías válidas exactas: 'Must-be', 'One-dimensional', 'Attractive', 'Indifferent', 'Reverse'."
    ),
    "Valor vs Complejidad": (
        "Eres un Agile Product Manager experto.\n"
        "Evalúa las Historias (JSON) usando Matriz Valor vs Complejidad.\n"
        "- value: 1 a 10.\n"
        "- complexity: 1 a 10.\n"
        "Devuelve JSON con 'results' (lista de {'id', 'score': {'value': float, 'complexity': float, "
        "'quadrant': 'str', 'rationale': 'str'}})\n"
        "Cuadrantes válidos exactos: 'Quick Win', 'Major Project', 'Fill In', 'Thankless Task'."
    ),
}

# ─── Parámetros de llamada al LLM ─────────────────────────────────────────────
CALL_PARAMS = {
    "temperature": LLM_TEMPERATURE_ANALYTICAL,
    "max_tokens": LLM_MAX_TOKENS_PRIORITIZE,
    "response_format": {"type": "json_object"},
}

# ─── Órdenes de clasificación para frameworks categóricos ─────────────────────
_MOSCOW_ORDER = {"Must Have": 1, "Should Have": 2, "Could Have": 3, "Won't Have": 4}
_KANO_ORDER = {"Must-be": 1, "One-dimensional": 2, "Attractive": 3, "Indifferent": 4, "Reverse": 5}
_VC_ORDER = {"Quick Win": 1, "Major Project": 2, "Fill In": 3, "Thankless Task": 4}


def build_payload(stories: List[UserStory]) -> str:
    """Construye el payload JSON mínimo para el LLM (solo id, title, description)."""
    return json.dumps([
        {"id": s.id, "title": s.title, "description": s.description}
        for s in stories if s.id
    ])


def parse_and_sort(content: str, stories: List[UserStory], framework: str) -> List[PrioritizedStory]:
    """Parsea la respuesta del LLM, construye PrioritizedStory y ordena por score."""
    data = json.loads(content)
    results_map = {item["id"]: item["score"] for item in data.get("results", [])}

    score_builders = {
        "RICE": lambda d: ("rice_score", RICEScore(**d)),
        "WSJF": lambda d: ("wsjf_score", WSJFScore(**d)),
        "MoSCoW": lambda d: ("moscow_score", MoSCoWScore(**d)),
        "Kano": lambda d: ("kano_score", KanoScore(**d)),
        "Valor vs Complejidad": lambda d: ("value_complexity_score", ValueComplexityScore(**d)),
    }

    prioritized = []
    for s in stories:
        if s.id not in results_map:
            continue
        try:
            p = PrioritizedStory(**s.model_dump())
            field, score_obj = score_builders[framework](results_map[s.id])
            setattr(p, field, score_obj)
            prioritized.append(p)
        except Exception as e:
            logger.warning(f"Error parseando score de {s.id}: {e}")

    return _sort(prioritized, framework)


def _sort(results: List[PrioritizedStory], framework: str) -> List[PrioritizedStory]:
    """Ordena los resultados según el framework aplicado."""
    if framework == "RICE":
        return sorted(results, key=lambda x: x.rice_score.total_score if x.rice_score else 0, reverse=True)
    if framework == "WSJF":
        return sorted(results, key=lambda x: x.wsjf_score.total_score if x.wsjf_score else 0, reverse=True)
    if framework == "MoSCoW":
        return sorted(results, key=lambda x: _MOSCOW_ORDER.get(x.moscow_score.category, 5) if x.moscow_score else 5)
    if framework == "Kano":
        return sorted(results, key=lambda x: _KANO_ORDER.get(x.kano_score.category, 6) if x.kano_score else 6)
    if framework == "Valor vs Complejidad":
        return sorted(results, key=lambda x: _VC_ORDER.get(x.value_complexity_score.quadrant, 5) if x.value_complexity_score else 5)
    return results
