from dataclasses import dataclass

from src.op_app.infrastructure.db.models.setor_model import SetorModel
from src.op_app.application.errors import ValidationError, ConflictError


@dataclass(frozen=True)
class CriarSetorInput:
    nome: str
    descricao: str | None = None


class CriarSetorUC:
    def execute(self, uow, data: CriarSetorInput) -> dict:
        nome = (data.nome or "").strip()
        descricao = (data.descricao or "").strip() or None

        if not nome:
            raise ValidationError(
                "Campo obrigatório: nome",
                details={"fields": ["nome"]}
            )

        if uow.setores.get_by_nome(nome):
            raise ConflictError(
                "Setor com esse nome já existe",
                details={"field": "nome", "value": nome}
            )

        setor = SetorModel(nome=nome, descricao=descricao, ativo=True)
        
        try:
            uow.setores.add(setor)  # repo faz flush -> pega id
        except IntegrityError:
            # se o banco acusar UNIQUE de qualquer jeito
            raise ConflictError("Setor com esse nome já existe", details={"field": "nome", "value": nome})


        return {
            "id": setor.id,
            "nome": setor.nome,
            "descricao": setor.descricao,
            "ativo": setor.ativo,
        }