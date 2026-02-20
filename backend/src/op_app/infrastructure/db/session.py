import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do banco de dados
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///op_app.db')

# Engine do SQLAlchemy
engine = create_engine(
    DATABASE_URL, 
    echo=False,  # Defina como True para ver as consultas SQL no console
    future=True
    )

# Session factory
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )

def get_session():
    """Retorna uma sessão (para uso em repositórios e UoW)."""
    return SessionLocal()

def remove_session():
    """Remove sessão do contexto atual (importante em apps web)."""
    SessionLocal.remove()


def get_engine():
    return engine