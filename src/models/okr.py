"""
Modelos Pydantic para el Generador de OKRs.
"""
from typing import List
from pydantic import BaseModel, Field

class KeyResult(BaseModel):
    title: str = Field(description="Título descriptivo del Key Result. Ej: Aumentar la tasa de retención mensual")
    metric_name: str = Field(description="Nombre corto de la métrica. Ej: Retención Mensual")
    baseline: float = Field(description="Valor actual o inicial de la métrica")
    target: float = Field(description="Valor objetivo a alcanzar")
    unit: str = Field(description="Unidad de medida (%, USD, usuarios, segundos, etc.)")
    initiatives: List[str] = Field(description="2 a 3 iniciativas o épicas clave para lograr este resultado")

class Objective(BaseModel):
    title: str = Field(description="Objetivo cualitativo, inspiracional y accionable (NO usar números aquí)")
    description: str = Field(description="Breve justificación de por qué este objetivo es crucial ahora")
    key_results: List[KeyResult] = Field(description="Lista de 3 a 5 Key Results asociados a este objetivo")

class OKRSet(BaseModel):
    timeframe: str = Field(description="Periodo o ciclo para estos OKRs (ej. Q3 2026)")
    strategic_alignment: str = Field(description="Breve resumen de cómo este set se alinea con la meta global de la empresa")
    objectives: List[Objective] = Field(description="Lista de 2 a 4 Objetivos principales")
