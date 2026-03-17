from datetime import datetime
from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from src.op_app.infrastructure.db.base import Base

class UsuarioModel(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    pin_hash: Mapped[str] = mapped_column("pin_hash", String(255), nullable=False)
    setor_id: Mapped[int] = mapped_column(ForeignKey("setores.id"), nullable=False)
    funcao_id: Mapped[int] = mapped_column(ForeignKey("funcoes.id"), nullable=False)
    ativo: Mapped[bool] = mapped_column(default=True, nullable=False)
    criado_em: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)

    setor = relationship("SetorModel", back_populates="usuarios")
    funcao = relationship("FuncaoModel", back_populates="usuarios")