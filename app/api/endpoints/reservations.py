"""Модуль для создания маршрутов."""

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from schemas.reservations import ReservationSchema
from core.db import db_session

router = APIRouter()


@router.get('/', response_model=ReservationSchema)
def get_reservations(self, session: AsyncSession = Depends(db_session)):
    """Маршрут для получения всех объектов."""
    pass


@router.post('/', response_model=ReservationSchema)
def create_reservation(self, session: AsyncSession = Depends(db_session)):
    """Маршрут для создания объекта."""
    pass


@router.delete('/{table_id}/', response_model=None)
def delete_reservation(
    self,
    reservation_id: int,
    session: AsyncSession = Depends(db_session)
):
    """Маршрут для удаления объекта."""
    pass
