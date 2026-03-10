from sqlalchemy.orm import Session
from src.op_app.infrastructure.db.models.funcao_model import FuncaoModel

class FuncaoRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, funcao: FuncaoModel) -> FuncaoModel:
        self.session.add(funcao)
        self.session.flush()
        return funcao

    def get_by_id(self, funcao_id: int) -> FuncaoModel | None:
        return self.session.get(FuncaoModel, funcao_id)
    
    def get_by_nome(self, nome: str) -> FuncaoModel | None:
        return self.session.query(FuncaoModel).filter(FuncaoModel.nome_funcao == nome).first()

    def list_all(self) -> list[FuncaoModel]:
        return self.session.query(FuncaoModel).order_by(FuncaoModel.nome_funcao.asc()).all()
    
    def update(self, funcao_id: int, data: dict) -> FuncaoModel | None:
        existing = self.session.get(FuncaoModel, funcao_id)
        if not existing:
            return None

        for field in ("nome_funcao",):
            if field in data:
                setattr(existing, field, data[field])

        return existing
    
    def delete(self, funcao_id: int) -> bool:
        existing = self.session.get(FuncaoModel, funcao_id)
        
        if not existing:
            return False
        
        self.session.delete(existing)
        return True