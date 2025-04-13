## 💻 Технологии:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=FastAPI&logoColor=56C0C0&color=008080)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat&logo=Pydantic&logoColor=56C0C0&color=008080)](https://pydantic-docs.helpmanual.io/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=56C0C0&color=008080)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat&logo=Alembic&logoColor=56C0C0&color=008080)](https://alembic.sqlalchemy.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)


## Описание reservation_table_test
"reservation_table_test" - это API приложение, где клиент может зарезервировать 
столик для своего досуга, посмотрев при этом все брони для столика, чтобы 
выбрать нужное для себя время. Так же удалить в случае, если клиент передумает. 
Есть так же сами столики, количество мест одного столика не превышает больше 
30 мест. Возможность просматривать все столики, которые по душе. Время работы 
ресторана с 8 до 23.

Доступные методы для всех ресурсов: GET, POST, DELETE

## Инструкция как развернуть проект в докере

- Нужно склонировать проект из репозитория командой:
```bash
git clone git@github.com:BogdanBrock/reserve_table_test.git
```
- Для развертывания проекта, в корне проекта нужно
создать .env файл, можно скопировать данные из .env.example

- Находясь так же в корне проекта нужно перейти
 в папку под названием "docker":
```bash
cd docker
```

- Выполнить команду с включенным докером:
```bash
docker compose up
```

- После того как докер запустился, нужно создать базу 
данных, миграции уже созданы, важно при этом, чтобы был 
запущен докер с контейнерами:
```bash
docker compose exec app alembic upgrade head
```

- Все маршруты доступны по адресу:
```bash
http://127.0.0.1:8000/docs#/
```
