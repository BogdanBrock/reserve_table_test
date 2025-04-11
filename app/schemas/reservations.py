"""Модуль reservations для создания схем."""

from datetime import datetime, timedelta

from pydantic import BaseModel, Field, computed_field

CUSTOMER_NAME_MAX_LENGTH = 64
DURATION_TIME_MAX_LENGTH = 64


class ReservationSchema(BaseModel):
    """Схема ReservationSchema для валидации, создания и отображение данных."""

    customer_name: str = Field(max_length=CUSTOMER_NAME_MAX_LENGTH)
    reservation_time: datetime
    duration_time: int = Field(max_length=DURATION_TIME_MAX_LENGTH)

    @computed_field
    def end_reservation_time(self) -> datetime:
        """Отображение конечного времени брони стола."""
        return self.reservation_time + timedelta(minutes=self.duration_time)
