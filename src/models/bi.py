"""
Modelos específicos para proyectos de Business Intelligence y PowerBI.
Extienden los modelos de dominio de agile.py sin modificarlos.
"""
from pydantic import Field
from typing import List

from src.models.agile import UserStory


class BIStory(UserStory):
    """Historia de usuario especializada para desarrollo en PowerBI/BI.
    
    Extiende UserStory con campos propios del ciclo de desarrollo BI:
    orígenes de datos, medidas DAX, tipo de visual y frecuencia de refresco.
    """
    data_sources: List[str] = Field(
        default_factory=list,
        description="Orígenes de datos necesarios (ej: SQL Server - tabla ventas)"
    )
    dax_measures: List[str] = Field(
        default_factory=list,
        description="Medidas DAX a crear o modificar (ej: [Total Ventas Netas] = SUMX(...))"
    )
    visual_type: str = Field(
        default="",
        description="Tipo de visual recomendado (ej: Gráfico de barras, Matriz, Tarjeta KPI)"
    )
    refresh_frequency: str = Field(
        default="Diaria",
        description="Frecuencia de actualización del dato (Tiempo real, Diaria, Semanal, Bajo demanda)"
    )
