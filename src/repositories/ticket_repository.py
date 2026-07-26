"""Repositorio de tickets — Interfaz abstracta (Repository Pattern).

Cualquier clase que implemente esta interfaz puede usarse como fuente de datos,
sin que la UI ni los servicios conozcan los detalles de implementación (Firebase,
Supabase, API REST, mock para tests...).
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional


class TicketRepository(ABC):

    @abstractmethod
    def get_projects(self) -> List[Dict[str, Any]]:
        """Devuelve la lista de proyectos disponibles."""
        ...

    @abstractmethod
    def get_epics(self, project_id: str) -> list:
        """Devuelve tickets de tipo épica del proyecto indicado."""
        ...

    @abstractmethod
    def get_stories(self, project_id: str) -> list:
        """Devuelve tickets priorizables (tareas, mejoras, desarrollos, entregables)."""
        ...

    @abstractmethod
    def save_ticket(self, project_id: str, ticket: Any) -> str:
        """Persiste un único ticket y devuelve su ID."""
        ...

    @abstractmethod
    def save_tickets_batch(self, project_id: str, tickets: list) -> List[str]:
        """Persiste múltiples tickets en paralelo y devuelve sus IDs."""
        ...

    @abstractmethod
    def update_ticket_score(self, project_id: str, ticket_id: str,
                            framework_field: str, score_data: Dict[str, Any]) -> None:
        """Actualiza el campo de scoring de un ticket concreto."""
        ...
