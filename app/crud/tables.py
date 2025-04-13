"""Модуль для создания CRUD операций."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import CRUDBase
from app.models import Table


class CRUDTable(CRUDBase):
    """Класс CRUDTable для создания CRUD операций."""

    async def get_table_by_name(
        self,
        name: str,
        session: AsyncSession
    ) -> Table | None:
        """Метод для получения стола по названию."""
        table = await session.execute(select(Table).where(Table.name == name))
        return table.scalar()


table_crud = CRUDTable(Table)
