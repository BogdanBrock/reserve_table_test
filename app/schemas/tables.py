"""Модуль для создания схем."""

from pydantic import BaseModel, Field, PositiveInt, field_validator

from app.api.exceptions import ValidationError

NAME_MAX_LENGTH = 64
LOCATION_MAX_LENGTH = 64
MAX_COUNT_SEATS = 30


class TableCreateSchema(BaseModel):
    """Схема TableCreateSchema для валидации, создания данных."""

    name: str = Field(max_length=NAME_MAX_LENGTH)
    seats: PositiveInt
    location: str = Field(max_length=LOCATION_MAX_LENGTH)

    @field_validator('seats', mode='after')
    @classmethod
    def validate_seats(cls, value) -> int | None:
        """Метод для валидации атрибута."""
        if value > MAX_COUNT_SEATS:
            raise ValidationError('У столика не может быть больше '
                                  f'{MAX_COUNT_SEATS} мест')
        return value


class TableReadSchema(BaseModel):
    """Схема TableReadSchema для чтения данных."""

    id: PositiveInt
    name: str
    seats: PositiveInt
    location: str
