"""
Modelos de dominio ágil.
Solo contiene entidades del negocio: Epic, UserStory, Subtask.
Los modelos de scoring viven en src/models/scores.py.
"""
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List, Any

from src.models.scores import RICEScore, WSJFScore, MoSCoWScore, KanoScore, ValueComplexityScore


class Subtask(BaseModel):
    id: str
    title: str
    completed: bool = False


class BaseTicket(BaseModel):
    # Ignora campos extra de Firebase sin romper la validación
    model_config = ConfigDict(extra='ignore')

    id: Optional[str] = Field(default=None, description="ID documento Firestore")
    code: Optional[str] = Field(default=None, description="ID visible en el tablero (ej: DA-027, TKT-55)")
    title: str = Field(default="Sin título")
    description: str = Field(default="")
    type: str = Field(default="tarea")
    status: str = Field(default="todo")
    priority: str = Field(default="medium")

    assignees: List[Any] = Field(default_factory=list)
    tags: List[Any] = Field(default_factory=list)
    acceptanceCriteria: List[Any] = Field(default_factory=list)
    comments: List[Any] = Field(default_factory=list)
    subtasks: List[Any] = Field(default_factory=list)  # Flexible: acepta cualquier estructura de Firestore

    createdAt: Optional[Any] = None
    updatedAt: Optional[Any] = None

    # Campos de scoring — uno por framework, nunca se sobreescriben entre sí
    rice_score: Optional[RICEScore] = None
    wsjf_score: Optional[WSJFScore] = None
    moscow_score: Optional[MoSCoWScore] = None
    kano_score: Optional[KanoScore] = None
    value_complexity_score: Optional[ValueComplexityScore] = None


class Epic(BaseTicket):
    type: str = Field(default="analisis")


class UserStory(BaseTicket):
    type: str = Field(description="Tipo de ticket: 'tarea', 'desarrollo', 'mejora', 'bug'")
    story_points: Optional[int] = Field(default=None)
    estimatedHours: Optional[int] = Field(default=None, description="Estimación en horas")


class PrioritizedStory(UserStory):
    """UserStory con al menos un score de framework calculado."""
    pass
