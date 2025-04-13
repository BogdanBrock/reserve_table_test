"""Модуль для создания схем."""

from datetime import datetime, time, timedelta

from pydantic import (BaseModel, Field, PositiveInt, computed_field,
                      field_validator, model_validator)

from app.api.exceptions import ValidationError
from app.models import Reservation

CUSTOMER_NAME_MAX_LENGTH = 64
FORMAT_TIME = '%d.%m.%y %H:%M'
START_WORKING = '8:00'
END_WORKING = '23:00'
MIN_DURATION_RESERVATION_TIME = 30
EXAMPLE_START_TIME = '18.04.25 19:30'
EXAMPLE_END_TIME = '18.04.25 20:00'


class ReservationCreateSchema(BaseModel):
    """Схема ReservationCreateSchema для валидации и создания данных."""

    customer_name: str = Field(max_length=CUSTOMER_NAME_MAX_LENGTH)
    reservation_time: str = Field(examples=[EXAMPLE_START_TIME])
    duration_minutes: PositiveInt = Field(
        examples=[MIN_DURATION_RESERVATION_TIME]
    )
    table_id: PositiveInt

    @property
    def reservation_end_time(self) -> datetime:
        """Атрибут для вычисления конечного времени брони стола."""
        return self.reservation_time + timedelta(minutes=self.duration_minutes)

    @model_validator(mode='after')
    def validate(self) -> Reservation | None:
        """Метод для валидации данных."""
        try:
            self.reservation_time = datetime.strptime(self.reservation_time,
                                                      FORMAT_TIME)
        except ValueError:
            raise ValidationError('Введите правильный формат даты, '
                                  f'как на примере: {EXAMPLE_START_TIME}')
        if self.duration_minutes < MIN_DURATION_RESERVATION_TIME:
            raise ValidationError('Нельзя зарезервировать столик меньше, чем '
                                  f'на {MIN_DURATION_RESERVATION_TIME} минут')
        start_time = self.reservation_time.time()
        end_time = self.reservation_end_time.time()
        for t in (start_time, end_time):
            if not (time(hour=START_WORKING) <= t <= time(hour=END_WORKING)):
                raise ValidationError('Нельзя забронировать столик '
                                      'в это время. Ресторан работает '
                                      f'с {START_WORKING} до {END_WORKING}')
        return self


class ReservationReadSchema(BaseModel):
    """Схема ReservationCreateSchema для чтения данных."""

    id: PositiveInt
    customer_name: str
    reservation_time: datetime = Field(examples=[EXAMPLE_START_TIME])
    duration_minutes: PositiveInt = Field(
        examples=[MIN_DURATION_RESERVATION_TIME]
    )
    table_id: PositiveInt

    @field_validator('reservation_time', mode='after')
    @classmethod
    def validate_reservation_time(cls, value) -> str:
        """Метод для преобразования даты в строку."""
        return datetime.strftime(value, FORMAT_TIME)

    @computed_field(examples=[EXAMPLE_END_TIME])
    def reservation_end_time(self) -> str:
        """Атрибут для отображение конечного времени брони стола."""
        reservation_end_time = datetime.strptime(
            self.reservation_time,
            FORMAT_TIME
        )
        reservation_end_time = reservation_end_time + timedelta(
            minutes=self.duration_minutes
        )
        return datetime.strftime(reservation_end_time, FORMAT_TIME)
