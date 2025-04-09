"""Модуль для настройки переменных окружения."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Класс для настройки переменных окружения."""

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    @property
    def db_url(self):
        """Атрибут для подключения к postgresql."""
        return ('postgresql+asyncpg://'
                f'{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@'
                f'{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}')


settings = Settings()
