from dataclasses import dataclass

from src.op_app.infrastructure.db.models.setor_model import SetorModel
from src.op_app.application.errors import ValidationError, ConflictError, IntegrityError


@dataclass(frozen=True)
class CriarSetorInput:
    nome: str
    codigo_setor: str | None = None
    ativo: bool = True

class CriarSetorUC:
    def execute(self, uow, data: CriarSetorInput) -> dict:
        nome = (data.nome or "").strip()
        codigo_setor = (data.codigo_setor or "").strip() or None
        ativo = True

        if not nome:
            raise ValidationError(
                "Campo obrigatório: nome",
                details={"fields": ["nome", "codigo_setor", "ativo"]}
            )

        if uow.setores.get_by_nome(nome):
            raise ConflictError(
                "Setor com esse nome já existe",
                details={"field": "nome", "value": nome}
            )

        setor = SetorModel(nome=nome, codigo_setor=codigo_setor, ativo=ativo)
        
        try:
            uow.setores.add(setor)  # repo faz flush -> pega id
        except IntegrityError:
            # se o banco acusar UNIQUE de qualquer jeito
            raise ConflictError("Setor com esse nome já existe", details={"field": "nome", "value": nome})


        return {
            "id": setor.id,
            "nome_setor": setor.nome,
            "codigo_setor": setor.codigo_setor,
            "ativo": setor.ativo
        }