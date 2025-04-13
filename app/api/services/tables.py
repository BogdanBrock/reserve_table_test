"""Модуль для создания сервиса."""

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.exceptions import NotFoundError, ValidationError
from app.crud import table_crud
from app.schemas import TableCreateSchema
from .base import BaseService
from app.models import Table


class TableService(BaseService):
    """Класс TableService для создания сервиса."""

    async def get_tables(
        self,
        session: AsyncSession
    ) -> list[Table]:
        """Метод для получения всех столиков."""
        return await self.crud.get_all(session)

    async def create_table(
        self,
        schema: TableCreateSchema,
        session: AsyncSession
    ) -> Table:
        """Метод для создания столика."""
        table = await self.crud.get_table_by_name(schema.name, session)
        if table:
            raise ValidationError('Нельзя создать один и тот же столик дважды')
        return await self.crud.create(schema, session)

    async def delete_table(
        self,
        table_id: int,
        session: AsyncSession
    ) -> None:
        """Метод для удаления столика."""
        table = await self.crud.get(table_id, session)
        if not table:
            raise NotFoundError('Такого столика не существует')
        await self.crud.delete(table, session)


table_service = TableService(table_crud)
