import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv

engine = None
SessionLocal = None

def init_session(database_url: str | None = None):
    """
    Inicializa engine e SessionLocal uma única vez.
    Chamar no create_app().
    """
    global engine, SessionLocal

    if engine is not None and SessionLocal is not None:
        return  # já inicializado

    # Carrega .env aqui somente se você REALMENTE precisar
    # Melhor ainda: carregar .env no entrypoint (run.py/wsgi.py)
    load_dotenv()

    db_url = database_url or os.getenv("DATABASE_URL", "sqlite:///op_app.db")

    engine = create_engine(
        db_url,
        echo=False,
        future=True,
        # Para SQLite em ambiente multi-thread/process, isso ajuda:
        connect_args={"check_same_thread": False} if db_url.startswith("sqlite") else {}
    )

    SessionLocal = scoped_session(
        sessionmaker(
            bind=engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )
    )

def get_session():
    if SessionLocal is None:
        raise RuntimeError("SessionLocal não inicializada. Chame init_session() no create_app().")
    return SessionLocal()

def remove_session():
    if SessionLocal is not None:
        SessionLocal.remove()

def get_engine():
    if engine is None:
        raise RuntimeError("Engine não inicializada. Chame init_session() no create_app().")
    return engine