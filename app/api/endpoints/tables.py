"""Модуль для создания маршрутов."""

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from schemas.tables import TableSchema
from core.db import db_session

router = APIRouter()


@router.get('/', response_model=TableSchema)
def get_tables(self, session: AsyncSession = Depends(db_session)):
    """Маршрут для получения всех объектов."""
    pass


@router.post('/', response_model=TableSchema)
def create_table(self, session: AsyncSession = Depends(db_session)):
    """Маршрут для создания объекта."""
    pass


@router.delete('/{table_id}/', response_model=None)
def delete_table(
    self,
    table_id: int,
    session: AsyncSession = Depends(db_session)
):
    """Маршрут для удаления объекта."""
    pass
