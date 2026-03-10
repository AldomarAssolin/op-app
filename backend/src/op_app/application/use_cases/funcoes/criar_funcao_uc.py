from dataclasses import dataclass

from src.op_app.infrastructure.db.models.setor_model import SetorModel
from src.op_app.infrastructure.db.models.funcao_model import FuncaoModel
from src.op_app.application.errors import ValidationError, ConflictError, IntegrityError

@dataclass(frozen=True)
class CriarFuncaoInput:
    nome_funcao: str
    
class CriarFuncaoUC:
    def execute(self, uow, data: CriarFuncaoInput) -> dict:
        nome_funcao = (data.nome_funcao or "").strip()

        if not nome_funcao:
            raise ValidationError(
                "Campo obrigatório: nome_funcao",
                details={"fields": ["nome_funcao"]}
            )

        if uow.funcoes.get_by_nome(nome_funcao):
            raise ConflictError(
                "Função com esse nome já existe",
                details={"field": "nome_funcao", "value": nome_funcao}
            )

        funcao = FuncaoModel(nome_funcao=nome_funcao)
        
        try:
            uow.funcoes.add(funcao)  # repo faz flush -> pega id
        except IntegrityError:
            # se o banco acusar UNIQUE de qualquer jeito
            raise ConflictError("Função com esse nome já existe", details={"field": "nome_funcao", "value": nome_funcao})

        return {
            "id": funcao.id,
            "nome": funcao.nome_funcao,
        }