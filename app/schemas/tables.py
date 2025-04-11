"""Модуль tables для создания схем."""

from pydantic import BaseModel, PositiveInt, Field

NAME_MAX_LENGTH = 64
LOCATION_MAX_LENGTH = 64
MIN_COUNT_SEATS = 30


class TableSchema(BaseModel):
    """Схема TableSchema для валидации, создания и отображение данных."""

    name: str = Field(max_length=NAME_MAX_LENGTH)
    seats: PositiveInt = Field(le=MIN_COUNT_SEATS)
    location: str = Field(max_length=LOCATION_MAX_LENGTH)
