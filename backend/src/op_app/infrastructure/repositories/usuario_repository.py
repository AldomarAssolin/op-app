from sqlalchemy.orm import Session
from src.op_app.infrastructure.db.models.usuario_model import UsuarioModel


class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, usuario: UsuarioModel) -> UsuarioModel:
        self.session.add(usuario)
        self.session.flush()
        return usuario

    def get_by_id(self, usuario_id: int) -> UsuarioModel | None:
        return self.session.get(UsuarioModel, usuario_id)

    def get_by_nome(self, nome: str) -> UsuarioModel | None:
        """Busca usuário por nome."""
        return self.session.query(UsuarioModel).filter(UsuarioModel.nome == nome).first()
    
    def update(self, usuario_id: int, data: dict) -> UsuarioModel | None:
        existing = self.session.get(UsuarioModel, usuario_id)
        if not existing:
            return None

        for field in ("nome", "funcao", "setor"):
            if field in data:
                setattr(existing, field, data[field])

        return existing
    
    def delete_by_id(self, usuario_id: int) -> bool:
        existing = self.session.get(UsuarioModel, usuario_id)
        
        if not existing:
            return False
        
        self.session.delete(existing)
        return True

    
    # def list(self,setor: str | None = None,funcao: str | None = None,nome: str | None = None) -> list[OperadorModel]:
    #     q = self.session.query(OperadorModel)
    #     if setor:
    #         q = q.filter(OperadorModel.setor == setor)
    #     if funcao:
    #         q = q.filter(OperadorModel.funcao == funcao)
    #     if nome:
    #         q = q.filter(OperadorModel.nome.ilike(f"%{nome}%"))
    #     return q.order_by(OperadorModel.id.asc()).all()