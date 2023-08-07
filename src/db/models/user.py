# шаблон создания модели таблицы базы данных

from sqlalchemy import Integer, BigInteger, Float, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    balance: Mapped[float] = mapped_column(Float, default=0)
