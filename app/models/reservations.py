"""Модуль reservations для создания моделей."""

from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base


class Reservation(Base):
    """Модель Reservation для создания таблицы в БД."""

    __tablename__ = 'reservations'

    customer_name: Mapped[str]
    reservation_time: Mapped[datetime]
    duration_minutes: Mapped[int]
    table_id: Mapped[int] = mapped_column(ForeignKey('tables.id'))

    table: Mapped['Table'] = relationship(
        'Table',
        back_populates='reservations'
    )
