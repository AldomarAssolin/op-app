from sqlalchemy.orm import Session
from ..db.models.operador_model import OperadorModel


class OperadorRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, operador: OperadorModel) -> OperadorModel:
        self.session.add(operador)
        self.session.flush()
        self.session.refresh(operador)
        return operador

    def get_by_id(self, operador_id: int) -> OperadorModel | None:
        return self.session.get(OperadorModel, operador_id)

    def list_all(self) -> list[OperadorModel]:
        return self.session.query(OperadorModel).order_by(OperadorModel.id.asc()).all()
    
    def update(self, operador_id: int, data: dict) -> OperadorModel | None:
        existing = self.session.get(OperadorModel, operador_id)
        if not existing:
            return None

        for field in ("nome", "funcao", "setor"):
            if field in data:
                setattr(existing, field, data[field])

        return existing
    
    def delete_by_id(self, operador_id: int) -> bool:
        existing = self.session.get(OperadorModel, operador_id)
        
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