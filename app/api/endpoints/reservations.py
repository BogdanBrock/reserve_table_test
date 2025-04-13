"""Модуль для создания маршрутов."""

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status

from app.api.services import reservation_service
from app.schemas import ReservationCreateSchema, ReservationReadSchema
from app.core.db import db_session

router = APIRouter()


@router.get(
    '/',
    response_model=list[ReservationReadSchema]
)
async def get_reservations(
    session: AsyncSession = Depends(db_session)
):
    """Маршрут для получения всех броней."""
    return await reservation_service.get_reservations(session)


@router.post(
    '/',
    response_model=ReservationReadSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_reservation(
    schema: ReservationCreateSchema,
    session: AsyncSession = Depends(db_session)
):
    """Маршрут для создания брони."""
    return await reservation_service.create_reservation(schema, session)


@router.delete(
    '/{reservation_id}/',
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_reservation(
    reservation_id: int,
    session: AsyncSession = Depends(db_session)
):
    """Маршрут для удаления брони."""
    await reservation_service.delete_reservation(
        reservation_id,
        session
    )
