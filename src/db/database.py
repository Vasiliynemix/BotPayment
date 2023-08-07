# Подключение к базе данных

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker

from src import conf


# Запускаю двигатель, с помощью которого я буду обращаться к базе данных
def async_engine(url: URL | str) -> AsyncEngine:
    return create_async_engine(url=url, echo=conf.logging.debug, pool_pre_ping=True)


# Сессия двигателя
def create_session_maker(engine: AsyncEngine | None) -> sessionmaker:
    return sessionmaker(
        engine,
        expire_on_commit=False,
        class_=AsyncSession
    )
