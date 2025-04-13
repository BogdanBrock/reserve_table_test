"""Модуль для создания исключений."""

from fastapi import HTTPException, status


class ValidationError(HTTPException):
    """Класс для создания исключения с ошибкой 400."""

    def __init__(self, detail: str | None = None):
        """Метод для инициализации объектов класса ValidationError."""
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST,
                         detail=detail)


class NotFoundError(HTTPException):
    """Класс для создания исключения с ошибкой 404."""

    def __init__(self, detail: str | None = None):
        """Метод для инициализации объектов класса NotFoundError."""
        super().__init__(status_code=status.HTTP_404_NOT_FOUND,
                         detail=detail)
