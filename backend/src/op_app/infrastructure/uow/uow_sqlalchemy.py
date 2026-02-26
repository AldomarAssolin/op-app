from src.op_app.infrastructure.db.session import get_session, remove_session
from src.op_app.infrastructure.repositories.operador_repository import OperadorRepository


class UnitOfWorkSQLAlchemy:
    def __init__(self):
        self.session = None
        self.operadores = None

    def __enter__(self):
        self.session = get_session()
        self.operadores = OperadorRepository(self.session)
        return self

    def __exit__(self, exc_type, exc, tb):
        try:
            if exc_type:
                self.session.rollback()
            else:
                self.session.commit()
        finally:
            self.session.close()
            remove_session()