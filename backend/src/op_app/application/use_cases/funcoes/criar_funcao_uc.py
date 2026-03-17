from dataclasses import dataclass

from src.op_app.domain.dto.FuncaoDTO import FuncaoDTO as Funcao
from src.op_app.interface.api.schemas.funcao_dto import FuncaoDTO
from src.op_app.infrastructure.db.models.funcao_model import FuncaoModel
from src.op_app.application.errors import ValidationError, ConflictError, IntegrityError


@dataclass(frozen=True)
class CriarFuncaoInput:
    """Input para criação de função."""
    nome_funcao: str


class CriarFuncaoUC:
    """Caso de uso para criar uma nova função."""

    def execute(self, uow, data: CriarFuncaoInput) -> FuncaoDTO:
        """Executa a criação da função com validações de unicidade e integridade."""
        # Sanitização
        nome_funcao = (data.nome_funcao or "").strip()

        # Validações de campos obrigatórios
        if not nome_funcao:
            raise ValidationError(
                "Campo obrigatório: nome_funcao",
                details={"fields": ["nome_funcao"]}
            )

        # Criar entidade de domínio (validações automáticas via __post_init__)
        try:
            funcao_entity = Funcao(
                nome_funcao=nome_funcao,
                id=None,
            )
        except ValueError as e:
            raise ValidationError(str(e), details={"field": "nome_funcao"})

        # Validar unicidade
        if uow.funcoes.get_by_nome(nome_funcao):
            raise ConflictError(
                "Função com esse nome já existe",
                details={"field": "nome_funcao", "value": nome_funcao}
            )

        # Mapear para modelo e adicionar via repositório
        funcao_model = FuncaoModel(nome_funcao=funcao_entity.nome_funcao)
        
        try:
            funcao_adicionada = uow.funcoes.add(funcao_model)
        except IntegrityError:
            # Se o banco acusar violação de constraint (fallback)
            raise ConflictError(
                "Função com esse nome já existe",
                details={"field": "nome_funcao", "value": nome_funcao}
            )

        # Retornar DTO
        return FuncaoDTO(
            id=funcao_adicionada.id,
            nome_funcao=funcao_adicionada.nome_funcao,
        )