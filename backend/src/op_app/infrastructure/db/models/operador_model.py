from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base


class OperadorModel(Base):
    __tablename__ = "operadores"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    funcao: Mapped[str] = mapped_column(String(60), nullable=False)
    setor_id: Mapped[int] = mapped_column(Integer, ForeignKey("setores.id"), nullable=False)
    
    setor = relationship("SetorModel")