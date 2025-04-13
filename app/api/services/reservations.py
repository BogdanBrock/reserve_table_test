"""Модуль для создания сервиса."""

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.exceptions import NotFoundError, ValidationError
from app.crud import reservation_crud, table_crud
from app.models import Reservation
from app.schemas import ReservationCreateSchema
from .base import BaseService


class ReservationService(BaseService):
    """Класс ReservationService для создания сервиса."""

    async def get_reservations(
        self,
        session: AsyncSession
    ) -> list[Reservation]:
        """Метод для получения всех броней."""
        return await self.crud.get_reservations_by_order_time(session)

    async def create_reservation(
        self,
        schema: ReservationCreateSchema,
        session: AsyncSession
    ) -> Reservation:
        """Метод для создания брони."""
        table = await table_crud.get(schema.table_id, session)
        if not table:
            raise NotFoundError('Такого столика не существует')
        reservation = await self.crud.get_reservation_by_time(schema, session)
        if reservation:
            raise ValidationError(
                'Нельзя зарезервировать на это время, т.к. ближайшая '
                f'бронь по времени с {reservation.reservation_time} по '
                f'{reservation.reservation_end_time}. Выберите другое время'
            )
        return await self.crud.create(schema, session)

    async def delete_reservation(
        self,
        reservation_id: int,
        session: AsyncSession
    ) -> None:
        """Метод для удаления брони."""
        reservation = await self.crud.get(reservation_id, session)
        if not reservation:
            raise NotFoundError('Такого зарезервированного '
                                'столика не существует')
        await self.crud.delete(reservation, session)


reservation_service = ReservationService(reservation_crud)
