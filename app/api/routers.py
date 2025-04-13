"""Модуль для создания основного маршрута."""

from fastapi import APIRouter

from app.api.endpoints import table_router, reservation_router

main_router = APIRouter(prefix='/api/v1')

main_router.include_router(
    table_router,
    prefix='/tables',
    tags=['Table']
)
main_router.include_router(
    reservation_router,
    prefix='/reservations',
    tags=['Reservation']
)
