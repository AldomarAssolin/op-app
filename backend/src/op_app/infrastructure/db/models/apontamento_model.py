from sqlalchemy import Column, Integer, BigInteger, DateTime, ForeignKey, CheckConstraint, Index
from sqlalchemy.sql import func
from src.op_app.infrastructure.db.base import Base

class ApontamentoProducaoModel(Base):
    __tablename__ = "apontamentos_producao"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    op_id = Column(Integer, ForeignKey("ordens_producao.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    etapa_id = Column(Integer, ForeignKey("etapas.id"), nullable=False)
    data_inicio = Column(DateTime, nullable=False, server_default=func.now())
    data_fim = Column(DateTime, nullable=True)
    
    __table_args__ = (
        CheckConstraint('data_fim > data_inicio', name='chk_datas_apontamento'),
        Index('idx_apontamento_op', 'op_id', 'data_inicio')
    )