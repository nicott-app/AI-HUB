from pydantic import BaseModel, Field

class SprintHealthDiagnosis(BaseModel):
    overall_status: str = Field(description="Estado general: 'Saludable', 'En Riesgo', o 'Crítico'")
    summary: str = Field(description="Resumen del diagnóstico del sprint/proyecto en lenguaje natural")
    bottlenecks: list[str] = Field(default_factory=list, description="Lista de cuellos de botella detectados")
    recommendations: list[str] = Field(default_factory=list, description="Lista de recomendaciones o acciones correctivas")
