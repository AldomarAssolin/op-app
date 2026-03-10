from src.op_app.infrastructure.db.session import get_session, remove_session
from src.op_app.infrastructure.repositories.usuario_repository import UsuarioRepository
from src.op_app.infrastructure.repositories.setor_repository import SetorRepository
from src.op_app.infrastructure.repositories.funcao_repository import FuncaoRepository


class UnitOfWorkSQLAlchemy:
    def __init__(self):
        self.session = None
        self.usuarios = None
        self.setores = None 
        self.funcoes = None

    def __enter__(self):
        self.session = get_session()
        self.usuarios = UsuarioRepository(self.session)
        self.setores = SetorRepository(self.session)
        self.funcoes = FuncaoRepository(self.session)
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