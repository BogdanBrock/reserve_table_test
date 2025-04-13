"""Модуль tables для создания моделей."""

from sqlalchemy.orm import Mapped, relationship

from app.core.db import Base


class Table(Base):
    """Модель Table для создания таблицы в БД."""

    __tablename__ = 'tables'

    name: Mapped[str]
    seats: Mapped[int]
    location: Mapped[str]

    reservations: Mapped[list['Reservation']] = relationship(
        'Reservation',
        back_populates='table',
        cascade='all, delete-orphan'
    )
