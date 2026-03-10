from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.op_app.infrastructure.db.base import Base

class UsuarioModel(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    pin: Mapped[str] = mapped_column(String(10), nullable=False)
    setor_id: Mapped[int] = mapped_column(ForeignKey("setores.id"), nullable=False)
    funcao_id: Mapped[int] = mapped_column(ForeignKey("funcoes.id"), nullable=False)

    setor = relationship("SetorModel", back_populates="usuarios")
    funcao = relationship("FuncaoModel", back_populates="usuarios")