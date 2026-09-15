from pydantic import BaseModel, Field

class QATestCase(BaseModel):
    title: str = Field(description="Título descriptivo del caso de prueba")
    test_type: str = Field(description="Tipo de prueba: 'Happy Path', 'Edge Case', 'Negative Flow'")
    gherkin_syntax: str = Field(description="Escenario en sintaxis Gherkin (Given-When-Then)")
