"""Модуль reservations для создания моделей."""

from datetime import datetime, timedelta

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property

from app.core.db import Base


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

    @hybrid_property
    def reservation_end_time(self) -> datetime:
        return self.reservation_time + timedelta(minutes=self.duration_minutes)

    @reservation_end_time.expression
    def reservation_end_time(cls) -> datetime:
        return cls.reservation_time + (
            cls.duration_minutes * text("INTERVAL '1 minute'")
        )
