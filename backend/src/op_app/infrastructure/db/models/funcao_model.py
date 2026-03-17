from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.op_app.infrastructure.db.base import Base

class FuncaoModel(Base):
    __tablename__ = "funcoes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome_funcao: Mapped[str] = mapped_column("nome", String(50), nullable=False, unique=True)

    usuarios = relationship("UsuarioModel", back_populates="funcao")