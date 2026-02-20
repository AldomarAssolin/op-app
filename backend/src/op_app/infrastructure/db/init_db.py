from src.op_app.infrastructure.db.session import get_engine
from src.op_app.infrastructure.db.base import Base

def init_db():
    """Cria todas as tabelas registradas nos modelos importados."""
    engine = get_engine()
    Base.metadata.create_all(bind=engine)