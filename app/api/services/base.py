"""Модуль для созданий базового сервиса."""

from typing import TypeVar

from app.crud import CRUDBase


CRUDType = TypeVar('CRUDType', bound=CRUDBase)


class BaseService:
    """Базовый сервис."""

    def __init__(self, crud: CRUDType):
        self.crud = crud
