from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.op_app.infrastructure.db.base import Base


class SetorModel(Base):
    __tablename__ = "setores"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    codigo_setor: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
    ativo: Mapped[bool] = mapped_column(nullable=False, default=True)

    usuarios = relationship("UsuarioModel", back_populates="setor")
    #ordens_producao = relationship("OrdemProducaoModel", back_populates="setor")