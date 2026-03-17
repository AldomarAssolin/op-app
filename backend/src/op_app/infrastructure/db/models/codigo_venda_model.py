from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.sql import func
from src.op_app.infrastructure.db.base import Base

class CodigoVendaModel(Base):
    __tablename__ = "codigos_venda"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo_venda = Column(String(50), nullable=False, unique=True)
    cliente = Column(String(100))
    data_pedido = Column(Date, server_default=func.current_date())