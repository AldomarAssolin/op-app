from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..base import Base


class TestTable(Base):
    __tablename__ = "test_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)