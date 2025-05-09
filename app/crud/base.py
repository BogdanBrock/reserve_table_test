"""Модуль для создания базовых CRUD операций."""

from typing import Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import Base

ModelType = TypeVar('ModelType', bound=Base)
SchemaType = TypeVar('SchemaType', bound=BaseModel)


class CRUDBase(Generic[ModelType, SchemaType]):
    """Базовый класс для создания CRUD операций."""

    def __init__(self, model: ModelType):
        """Метод для инициализации атрибутов объекта класса CRUDBase."""
        self.model = model

    async def get_all(
        self,
        session: AsyncSession
    ) -> list[ModelType]:
        """Метод для получения всех объектов."""
        model_objs = await session.execute(select(self.model))
        return model_objs.scalars().all()

    async def get(
        self,
        id: int,
        session: AsyncSession
    ) -> ModelType | None:
        """Метод для получения объекта."""
        model_obj = await session.execute(
            select(self.model).
            where(self.model.id == id)
        )
        return model_obj.scalar()

    async def create(
        self,
        schema: SchemaType,
        session: AsyncSession
    ) -> ModelType:
        """Метод для создания объекта."""
        model_obj = self.model(**schema.model_dump())
        session.add(model_obj)
        await session.commit()
        await session.refresh(model_obj)
        return model_obj

    async def delete(
        self,
        model_obj: ModelType,
        session: AsyncSession
    ) -> None:
        """Метод для удаления объекта."""
        await session.delete(model_obj)
        await session.commit()
