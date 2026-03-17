from sqlalchemy import Column, Integer, String
from src.op_app.infrastructure.db.base import Base

class EtapaModel(Base):
    __tablename__ = "etapas"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_etapa = Column(String(50), nullable=False)
    ordem_fluxo = Column(Integer, nullable=False, unique=True)