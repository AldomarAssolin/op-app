from src.op_app.infrastructure.db.session import init_session, get_engine
from src.op_app.infrastructure.db.base import Base

# importa models para registrar no Base.metadata
from src.op_app.infrastructure.db.models.operador_model import OperadorModel
from src.op_app.infrastructure.db.models.setor_model import SetorModel

def main():
    init_session()
    engine = get_engine()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("✅ Banco recriado com sucesso.")

if __name__ == "__main__":
    main()