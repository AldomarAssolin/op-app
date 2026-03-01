from dataclasses import dataclass

from src.op_app.infrastructure.db.models.operador_model import OperadorModel
from src.op_app.application.errors import ValidationError, NotFoundError

@dataclass(frozen=True)
class CriarOperadorInput:
    nome: str
    funcao: str
    setor_id: int


class CriarOperadorUC:
    def execute(self, uow, data: CriarOperadorInput) -> dict:
        nome = (data.nome or "").strip()
        funcao = (data.funcao or "").strip()
        setor_id = data.setor_id 

        # setor_id pode vir como int, mas às vezes chega string no JSON
        try:
            setor_id = int(data.setor_id)
        except (TypeError, ValueError):
            raise ValidationError(
                "setor_id inválido",
                details={"field": "setor_id", "hint": "Envie um inteiro válido"},
            )

        if not nome or not funcao:
            raise ValidationError(
                "Campos obrigatórios: nome, funcao, setor_id",
                details={"fields": ["nome", "funcao", "setor_id"]},
            )

        # valida se o setor existe
        setor = uow.setores.get_by_id(setor_id)
        if not setor:
            raise NotFoundError("Setor não encontrado", details={"setor_id": setor_id})

        operador = OperadorModel(nome=nome, funcao=funcao, setor_id=setor_id)
        operador = uow.operadores.add(operador) 

        return {
            "id": operador.id,
            "nome": operador.nome,
            "funcao": operador.funcao,
            "setor_id": operador.setor_id,
        }