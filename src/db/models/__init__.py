# Инициализация всех моделей для корректной работы alembic

from .base import Base
from .user import User

__all__ = ('Base', 'User', )
