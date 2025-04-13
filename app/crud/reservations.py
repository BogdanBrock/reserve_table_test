"""Модуль для создания CRUD операций."""

from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Reservation
from app.schemas import ReservationCreateSchema
from .base import CRUDBase


class CRUDReservation(CRUDBase):
    """Класс CRUDReservation для создания CRUD операций."""

    async def get_reservations_by_order_time(
        self,
        session: AsyncSession
    ) -> list[Reservation]:
        """Метод для получения всех отсортированных броней по времени."""
        reservations = await session.execute(
            select(Reservation).
            order_by(Reservation.reservation_time)
        )
        return reservations.scalars().all()

    async def get_reservation_by_time(
        self,
        schema: ReservationCreateSchema,
        session: AsyncSession
    ) -> Reservation:
        """Метод для получения брони по временному промежутку."""
        reversation = await session.execute(
            select(Reservation).
            where(
                or_(
                    Reservation.reservation_time.between(
                        schema.reservation_time,
                        schema.reservation_end_time
                    ),
                    Reservation.reservation_end_time.between(
                        schema.reservation_time,
                        schema.reservation_end_time
                    )
                )
            )
        )
        return reversation.scalar()


reservation_crud = CRUDReservation(Reservation)
