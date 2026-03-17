import enum
from sqlalchemy import Column, Integer, BigInteger, String, Enum, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.sql import func
from src.op_app.infrastructure.db.base import Base

class StatusOPEnum(enum.Enum):
    AGUARDANDO = 'AGUARDANDO'
    EM_PRODUCAO = 'EM_PRODUCAO'
    PARADO = 'PARADO'
    CONCLUIDO = 'CONCLUIDO'

class OrdemProducaoModel(Base):
    __tablename__ = "ordens_producao"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    cv_id = Column(Integer, ForeignKey("codigos_venda.id"), nullable=False)
    etapa_atual_id = Column(Integer, ForeignKey("etapas.id"), nullable=False)
    numero_op = Column(BigInteger, nullable=False, unique=True)
    sequencia_op = Column(Integer, nullable=False)
    status_op = Column(Enum(StatusOPEnum), default=StatusOPEnum.AGUARDANDO, index=True)
    data_criacao = Column(DateTime, server_default=func.now())

    __table_args__ = (
        UniqueConstraint('cv_id', 'sequencia_op', name='uq_cv_sequencia'),
    )