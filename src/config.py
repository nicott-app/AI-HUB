"""
Configuración centralizada de la aplicación.
Todos los valores configurables deben vivir aquí, nunca hardcodeados en el código.
"""

# ─── LLM ──────────────────────────────────────────────────────────────────────
LLM_MODEL = "llama-3.3-70b-versatile"
LLM_TEMPERATURE_CREATIVE = 0.3   # Para generación creativa (troceador)
LLM_TEMPERATURE_ANALYTICAL = 0.2 # Para análisis estructurado (priorizadores)
LLM_MAX_TOKENS_EPIC = 2048
LLM_MAX_TOKENS_PRIORITIZE = 4000

# ─── Firebase / Data ───────────────────────────────────────────────────────────
TICKET_QUERY_LIMIT = 200
EPIC_TYPES = ["analisis", "desarrollo"]
STORY_TYPES = ["tarea", "mejora", "desarrollo", "entregable"]
DONE_STATUSES = ["done"]

# ─── Cache ─────────────────────────────────────────────────────────────────────
CACHE_TTL_SECONDS = 300  # 5 minutos

# ─── Concurrencia ──────────────────────────────────────────────────────────────
MAX_PARALLEL_WORKERS = 8
