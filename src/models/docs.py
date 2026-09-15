from pydantic import BaseModel, Field

class ReleaseNotes(BaseModel):
    version: str = Field(description="Versión del lanzamiento (ej. v1.0)")
    summary: str = Field(description="Resumen ejecutivo del lanzamiento")
    features: list[str] = Field(default_factory=list, description="Lista de nuevas funcionalidades y mejoras")
    technical_details: list[str] = Field(default_factory=list, description="Detalles técnicos, deuda técnica resuelta o bugs corregidos")
    markdown_content: str = Field(description="Contenido completo en formato Markdown listo para copiar y pegar")
