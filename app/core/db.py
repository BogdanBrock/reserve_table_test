"""Модуль для создания базовой модели и фабрики сессий."""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (AsyncAttrs, AsyncSession,
                                    async_sessionmaker, create_async_engine)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from .config import settings


engine = create_async_engine(settings.db_url, echo=True)

async_session_maker = async_sessionmaker(engine,
                                         expire_on_commit=False,
                                         class_=AsyncSession)


async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """Функция для создания сессий."""
    with async_session_maker() as session:
        yield session


class Base(AsyncAttrs, DeclarativeBase):
    """Базовая модель Base."""

    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
