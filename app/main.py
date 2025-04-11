"""Модуль для создания экземпляра приложения. Основная точка входа."""

from fastapi import FastAPI

from api.routers import main_router

app = FastAPI()

app.include_router(main_router)
