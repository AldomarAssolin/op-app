from dataclasses import dataclass

from src.op_app.domain.dto.SetorDTO import SetorDTO as Setor
from src.op_app.interface.api.schemas.setor_dto import SetorDTO
from src.op_app.infrastructure.db.models.setor_model import SetorModel
from src.op_app.application.errors import ValidationError, ConflictError, IntegrityError


@dataclass(frozen=True)
class CriarSetorInput:
    """Input para criação de setor."""
    nome: str
    codigo_setor: str
    ativo: bool = True


class CriarSetorUC:
    """Caso de uso para criar um novo setor."""

    def execute(self, uow, data: CriarSetorInput) -> SetorDTO:
        """Executa a criação do setor com validações de unicidade e integridade."""
        # Sanitização
        nome = (data.nome or "").strip()
        codigo_setor = (data.codigo_setor or "").strip()
        ativo = data.ativo

        # Validações de campos obrigatórios
        if not nome or not codigo_setor:
            raise ValidationError(
                "Campos obrigatórios: nome, codigo_setor",
                details={"fields": ["nome", "codigo_setor"]}
            )

        # Criar entidade de domínio (validações automáticas via __post_init__)
        try:
            setor_entity = Setor(
                nome=nome,
                codigo_setor=codigo_setor,
                ativo=ativo,
                id=None,
            )
        except ValueError as e:
            raise ValidationError(str(e), details={"field": str(e).split()[0].lower()})

        # Validar unicidade do nome
        if uow.setores.get_by_nome(nome):
            raise ConflictError(
                "Setor com esse nome já existe",
                details={"field": "nome", "value": nome}
            )

        # Validar unicidade do código (será capturada pelo banco também como constraint)
        if uow.setores.get_by_codigo(codigo_setor):
            raise ConflictError(
                "Setor com esse código já existe",
                details={"field": "codigo_setor", "value": codigo_setor}
            )

        # Mapear para modelo e adicionar via repositório
        setor_model = SetorModel(
            nome=setor_entity.nome,
            codigo_setor=setor_entity.codigo_setor,
            ativo=setor_entity.ativo,
        )
        
        try:
            setor_adicionado = uow.setores.add(setor_model)
        except IntegrityError:
            # Se o banco acusar violação de constraint (fallback)
            raise ConflictError(
                "Erro ao criar setor: verificar unicidade de código",
                details={"field": "codigo_setor"}
            )

        # Retornar DTO
        return SetorDTO(
            id=setor_adicionado.id,
            nome=setor_adicionado.nome,
            codigo_setor=setor_adicionado.codigo_setor,
            ativo=setor_adicionado.ativo,
        )