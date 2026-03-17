import os
from sqlalchemy import text
from src.op_app.infrastructure.db.session import init_session, get_engine
from dotenv import load_dotenv

def test_connection():
    print("Carregando variáveis de ambiente...")
    load_dotenv()
    
    db_url = os.getenv('DATABASE_URL')
    print(f"DATABASE_URL detectada: {db_url}")
    
    print("Inicializando a engine do SQLAlchemy...")
    init_session()
    engine = get_engine()
    
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print(f"Sucesso! Conectado ao banco de dados. Resposta do banco: {result.scalar()}")
    except Exception as e:
        print(f"Erro ao conectar com o banco de dados:\n{e}")

if __name__ == "__main__":
    test_connection()
    