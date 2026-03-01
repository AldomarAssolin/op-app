from sqlalchemy.orm import Session
from src.op_app.infrastructure.db.models.setor_model import SetorModel


class SetorRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, setor: SetorModel) -> SetorModel:
        self.session.add(setor)
        self.session.flush()
        return setor

    def get_by_id(self, setor_id: int) -> SetorModel | None:
        return self.session.get(SetorModel, setor_id)
    
    def get_by_nome(self, nome: str) -> SetorModel | None:
        return self.session.query(SetorModel).filter(SetorModel.nome == nome).first()

    def list_all(self) -> list[SetorModel]:
        return self.session.query(SetorModel).order_by(SetorModel.nome.asc()).all()
    
    def update(self, setor_id: int, data: dict) -> SetorModel | None:
        existing = self.session.get(SetorModel, setor_id)
        if not existing:
            return None

        for field in ("nome", "descricao"):
            if field in data:
                setattr(existing, field, data[field])

        return existing
    
    def delete_by_id(self, setor_id: int) -> bool:
        existing = self.session.get(SetorModel, setor_id)
        
        if not existing:
            return False
        
        self.session.delete(existing)
        return True