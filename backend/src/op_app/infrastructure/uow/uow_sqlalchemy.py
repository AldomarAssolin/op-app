from src.op_app.infrastructure.db.session import get_session, remove_session
from src.op_app.infrastructure.repositories.operador_repository import OperadorRepository
from src.op_app.infrastructure.repositories.setor_repository import SetorRepository


class UnitOfWorkSQLAlchemy:
    def __init__(self):
        self.session = None
        self.operadores = None
        self.setores = None  # Adicionei o repositório de setores aqui

    def __enter__(self):
        self.session = get_session()
        self.operadores = OperadorRepository(self.session)
        self.setores = SetorRepository(self.session)  # Inicialize o repositório de setores aqui
        return self

    def __exit__(self, exc_type, exc, tb):
        try:
            if exc_type:
                self.session.rollback()
                return False  # re-raise a exceção original

            try:
                self.session.commit()
            except Exception:
                self.session.rollback()
                raise

        finally:
            self.session.close()