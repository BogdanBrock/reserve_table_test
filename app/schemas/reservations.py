"""Модуль reservations для создания схем."""

from datetime import datetime, timedelta, time

from fastapi import HTTPException, status
from pydantic import (BaseModel, PositiveInt, Field,
                      computed_field, model_validator)

CUSTOMER_NAME_MAX_LENGTH = 64
DURATION_TIME_MAX_LENGTH = 64


class ReservationSchema(BaseModel):
    """Схема ReservationSchema для валидации, создания и отображение данных."""

    customer_name: str = Field(max_length=CUSTOMER_NAME_MAX_LENGTH)
    reservation_time: datetime
    duration_time: PositiveInt
    table_id: PositiveInt

    @property
    def time_end(self) -> datetime:
        """Атрибут для вычисления времени окончания"""
        return self.reservation_time + timedelta(minutes=self.duration_time)

    @model_validator(mode='after')
    def validate(self):
        """Метод для валидации данных."""
        for t in (self.reservation_time.time(), self.time_end.time()):
            if not (time(hour=8) <= t <= time(hour=23)):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail='Нельзя забронировать, '
                                           'в это время ресторан не работает')

    @computed_field
    def reservation_end_time(self) -> datetime:
        """Отображение конечного времени брони стола."""
        return self.time_end
