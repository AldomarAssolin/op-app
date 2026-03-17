from dataclasses import dataclass

from src.op_app.domain.dto.UsuarioDTO import UsuarioDTO as Usuario
from src.op_app.interface.api.schemas.usuario_dto import UsuarioDTO
from src.op_app.infrastructure.db.models.usuario_model import UsuarioModel
from src.op_app.application.errors import ValidationError, NotFoundError


@dataclass(frozen=True)
class CriarUsuarioInput:
    """Input para criação de usuário."""
    nome: str
    pin: str
    funcao_id: int
    setor_id: int


class CriarUsuarioUC:
    """Caso de uso para criar um novo usuário."""

    def execute(self, uow, data: CriarUsuarioInput) -> UsuarioDTO:
        """Executa a criação do usuário com validações de negócio."""
        # Validações básicas e sanitização
        nome = (data.nome or "").strip()
        pin = (data.pin or "").strip()
        funcao_id = data.funcao_id
        setor_id = data.setor_id

        # Validações de campos obrigatórios
        if not nome or not pin:
            raise ValidationError(
                "Campos obrigatórios: nome, pin",
                details={"fields": ["nome", "pin"]},
            )

        # Validações de negócio adicionais
        if len(pin) < 4:
            raise ValidationError(
                "PIN deve ter pelo menos 4 caracteres",
                details={"field": "pin", "hint": "Use pelo menos 4 dígitos"},
            )

        # Verificar unicidade do nome (simples, pode ser otimizado com índice)
        existing_usuario = uow.usuarios.get_by_nome(nome)
        if existing_usuario:
            raise ValidationError(
                "Nome já existe",
                details={"field": "nome", "hint": "Escolha um nome único"},
            )

        # Verificar existência de setor e função
        setor = uow.setores.get_by_id(setor_id)
        if not setor:
            raise NotFoundError("Setor não encontrado", details={"setor_id": setor_id})

        funcao = uow.funcoes.get_by_id(funcao_id)
        if not funcao:
            raise NotFoundError("Função não encontrada", details={"funcao_id": funcao_id})

        # Criar entidade de domínio (validações automáticas via __post_init__)
        try:
            usuario_entity = Usuario(
                id=None,  # Será gerado pelo banco
                nome=nome,
                pin=pin,
                funcao_id=funcao_id,
                setor_id=setor_id,
            )
        except ValueError as e:
            raise ValidationError(str(e), details={"field": str(e).split()[0].lower()})

        # Mapear para modelo e adicionar via repositório
        usuario_model = UsuarioModel(
            nome=usuario_entity.nome,
            pin=usuario_entity.pin,
            funcao_id=usuario_entity.funcao_id,
            setor_id=usuario_entity.setor_id,
        )
        usuario_adicionado = uow.usuarios.add(usuario_model)

        # Retornar DTO
        return UsuarioDTO(
            id=usuario_adicionado.id,
            nome=usuario_adicionado.nome,
            pin=usuario_adicionado.pin,
            funcao_id=usuario_adicionado.funcao_id,
            setor_id=usuario_adicionado.setor_id,
        )