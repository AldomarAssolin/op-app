from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class OperadorModel(Base):
    __tablename__ = "operadores"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    funcao: Mapped[str] = mapped_column(String(60), nullable=False)   # Montador, Soldador, Inspetor...
    setor: Mapped[str] = mapped_column(String(60), nullable=False)    # Montagem, Soldagem, Inspeção...