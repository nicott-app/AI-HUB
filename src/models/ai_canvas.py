"""
Modelos de dominio para el Canvas de Proyecto IA.
"""
from pydantic import BaseModel, Field
from typing import List, Optional


class AIProjectCanvas(BaseModel):
    """Representa un Canvas completo para un proyecto de IA."""

    # ── Bloque 1: Problema ────────────────────────────────────────────────────
    problem_statement: str = Field(description="Descripción concisa del problema de negocio a resolver")
    affected_users: str = Field(description="Quién se ve afectado por el problema (roles, departamentos)")
    current_pain: str = Field(description="Impacto actual del problema: tiempo perdido, coste, riesgo...")

    # ── Bloque 2: Solución IA ─────────────────────────────────────────────────
    proposed_solution: str = Field(description="Descripción de la solución de IA propuesta")
    ai_approach: str = Field(description="Tipo de IA / enfoque técnico recomendado")
    alternatives_considered: List[str] = Field(description="Alternativas no-IA consideradas y por qué se descartaron")

    # ── Bloque 3: Datos ───────────────────────────────────────────────────────
    data_sources: List[str] = Field(description="Fuentes de datos necesarias y su estado de disponibilidad")
    data_volume: str = Field(description="Volumen estimado de datos (ej: 50.000 registros históricos)")
    data_quality_risks: List[str] = Field(description="Riesgos conocidos sobre la calidad o disponibilidad de los datos")

    # ── Bloque 4: Métricas de éxito ───────────────────────────────────────────
    primary_kpi: str = Field(description="KPI principal de éxito del proyecto")
    secondary_kpis: List[str] = Field(description="KPIs secundarios de seguimiento")
    baseline: str = Field(description="Situación actual (punto de partida medible)")
    target: str = Field(description="Objetivo cuantificado a alcanzar")

    # ── Bloque 5: Equipo y recursos ───────────────────────────────────────────
    team_needed: List[str] = Field(description="Roles necesarios para el proyecto (ej: Data Engineer, PM, Domain Expert)")
    infrastructure: str = Field(description="Infraestructura requerida (cloud, on-premise, GPU, etc.)")
    estimated_budget: str = Field(description="Rango de inversión estimada")

    # ── Bloque 6: Riesgos ─────────────────────────────────────────────────────
    risks: List[dict] = Field(description="Lista de riesgos con su probabilidad, impacto y plan de mitigación")

    # ── Bloque 7: Roadmap ─────────────────────────────────────────────────────
    phases: List[dict] = Field(description="Fases del proyecto con nombre, duración y entregables clave")
    total_duration: str = Field(description="Duración total estimada del proyecto")

    # ── Bloque 8: Valor de negocio ────────────────────────────────────────────
    business_value: str = Field(description="Valor estratégico y/o económico del proyecto para la organización")
    roi_estimate: str = Field(description="Estimación del ROI esperado (cuantitativo o cualitativo)")
