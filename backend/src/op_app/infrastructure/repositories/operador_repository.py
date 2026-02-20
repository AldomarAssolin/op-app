from sqlalchemy.orm import Session
from ..db.models.operador_model import OperadorModel


class OperadorRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, operador: OperadorModel) -> OperadorModel:
        self.session.add(operador)
        return operador

    def get_by_id(self, operador_id: int) -> OperadorModel | None:
        return self.session.get(OperadorModel, operador_id)

    def list_all(self) -> list[OperadorModel]:
        return self.session.query(OperadorModel).order_by(OperadorModel.id.asc()).all()