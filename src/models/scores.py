"""
Modelos de scoring/priorización.
Separados de agile.py porque son modelos de respuesta de la API del LLM,
no modelos de dominio ágil puro.
"""
from pydantic import BaseModel, Field


class RICEScore(BaseModel):
    reach: float = Field(default=1.0)
    impact: float = Field(default=1.0)
    confidence: float = Field(default=100.0)
    effort: float = Field(default=1.0)
    total_score: float = Field(default=0.0)
    rationale: str = Field(default="")


class WSJFScore(BaseModel):
    user_business_value: float = Field(default=1.0)
    time_criticality: float = Field(default=1.0)
    risk_reduction_opportunity: float = Field(default=1.0)
    job_size: float = Field(default=1.0)
    total_score: float = Field(default=0.0, description="(UBV+TC+RRO) / JobSize")
    rationale: str = Field(default="")


class MoSCoWScore(BaseModel):
    category: str = Field(default="Could Have",
                          description="Must Have | Should Have | Could Have | Won't Have")
    rationale: str = Field(default="")


class KanoScore(BaseModel):
    category: str = Field(default="Indifferent",
                          description="Must-be | One-dimensional | Attractive | Indifferent | Reverse")
    rationale: str = Field(default="")


class ValueComplexityScore(BaseModel):
    value: float = Field(default=1.0, description="1-10")
    complexity: float = Field(default=1.0, description="1-10")
    quadrant: str = Field(default="Low Value, High Complexity",
                          description="Quick Win | Major Project | Fill In | Thankless Task")
    rationale: str = Field(default="")
