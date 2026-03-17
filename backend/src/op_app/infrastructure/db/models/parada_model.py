from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.sql import func
from src.op_app.infrastructure.db.base import Base

class CategoriaParadaModel(Base):
    __tablename__ = "categorias_parada"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_categoria = Column(String(50), nullable=False)

class MotivoParadaModel(Base):
    __tablename__ = "motivos_parada"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria_id = Column(Integer, ForeignKey("categorias_parada.id"), nullable=False)
    descricao = Column(String(100), nullable=False)

class RegistroParadaModel(Base):
    __tablename__ = "registros_parada"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    op_id = Column(Integer, ForeignKey("ordens_producao.id"), nullable=False, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    motivo_id = Column(Integer, ForeignKey("motivos_parada.id"), nullable=False)
    data_inicio = Column(DateTime, nullable=False, server_default=func.now())
    data_fim = Column(DateTime, nullable=True)
    
    __table_args__ = (
        CheckConstraint('data_fim > data_inicio', name='chk_datas_parada'),
    )