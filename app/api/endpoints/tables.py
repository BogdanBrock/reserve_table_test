"""Модуль для создания маршрутов."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.services import table_service
from app.core.db import db_session
from app.schemas import TableCreateSchema, TableReadSchema

router = APIRouter()


@router.get(
    '/',
    response_model=list[TableReadSchema]
)
async def get_tables(
    session: AsyncSession = Depends(db_session)
):
    """Маршрут для получения всех столиков."""
    return await table_service.get_tables(session)


@router.post(
    '/',
    response_model=TableReadSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_table(
    schema: TableCreateSchema,
    session: AsyncSession = Depends(db_session)
):
    """Маршрут для создания столика."""
    return await table_service.create_table(schema, session)


@router.delete(
    '/{table_id}/',
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_table(
    table_id: int,
    session: AsyncSession = Depends(db_session)
):
    """Маршрут для удаления столика."""
    await table_service.delete_table(table_id, session)
