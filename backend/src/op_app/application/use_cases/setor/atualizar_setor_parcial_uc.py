from src.op_app.application.errors import ValidationError, NotFoundError, ConflictError
from src.op_app.interface.api.schemas.setor_dto import SetorDTO

class AtualizarSetorParcialUC:
    def execute(self, uow, setor_id: int, payload: dict) -> SetorDTO:
        setor = uow.setores.get_by_id(setor_id)

        if not setor:
            raise NotFoundError("Setor não encontrado", details={"setor_id": setor_id})

        if "nome" in payload or "codigo_setor" in payload:
            nome = (payload.get("nome") or "").strip()
            codigo_setor = (payload.get("codigo_setor") or "").strip() or None

            existente = uow.setores.get_by_nome(nome)
            if existente and existente.id != setor_id:
                raise ConflictError("Já existe um setor com esse nome", details={"nome": nome})

            setor.nome = nome
            setor.codigo_setor = codigo_setor

        if "ativo" in payload:
            ativo = payload.get("ativo")
            if not isinstance(ativo, bool):
                raise ValidationError("ativo deve ser boolean", details={"field": "ativo"})
            setor.ativo = ativo
            
        if not setor.nome:
            setor.nome = setor.nome.strip()
            
        
        return SetorDTO(
            id=setor.id,
            nome=setor.nome,
            codigo_setor=setor.codigo_setor,
            ativo=setor.ativo
        )