"""
Modelos de dominio para el Generador de Casos de Uso de IA.
"""
from pydantic import BaseModel, Field
from typing import List, Optional


class AIUseCase(BaseModel):
    """Representa un caso de uso de IA generado para una organización."""
    title: str = Field(description="Nombre del caso de uso")
    description: str = Field(description="Qué problema resuelve y cómo")
    business_area: str = Field(description="Área de negocio afectada (ej: Ventas, RRHH, Operaciones)")
    ai_type: str = Field(description="Tipo de IA recomendada (ej: NLP, Computer Vision, Forecasting, Automatización RPA)")
    estimated_impact: str = Field(description="Impacto estimado: Alto / Medio / Bajo")
    estimated_effort: str = Field(description="Esfuerzo estimado de implementación: Alto / Medio / Bajo")
    time_to_value: str = Field(description="Tiempo estimado hasta resultados visibles (ej: 1-3 meses)")
    kpis: List[str] = Field(description="KPIs que mejoraría este caso de uso")
    prerequisites: List[str] = Field(description="Requisitos previos de datos, infraestructura o equipo")
    priority_score: Optional[float] = Field(default=None, description="Score de priorización calculado (impacto/esfuerzo)")
