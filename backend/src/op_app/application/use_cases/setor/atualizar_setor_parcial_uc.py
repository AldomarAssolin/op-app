from src.op_app.application.errors import ValidationError, NotFoundError, ConflictError

class AtualizarSetorParcialUC:
    def execute(self, uow, setor_id: int, payload: dict) -> dict:
        setor = uow.setores.get_by_id(setor_id)

        if not setor:
            raise NotFoundError("Setor não encontrado", details={"setor_id": setor_id})

        if "nome" in payload or "descricao" in payload:
            nome = (payload.get("nome") or "").strip()
            descricao = (payload.get("descricao") or "").strip() or None
            
            if not nome:
                raise ValidationError("nome não pode ser vazio", details={"field": "nome"})

            existente = uow.setores.get_by_nome(nome)
            if existente and existente.id != setor_id:
                raise ConflictError("Já existe um setor com esse nome", details={"nome": nome})

            setor.nome = nome
            setor.descricao = descricao

        if "ativo" in payload:
            ativo = payload.get("ativo")
            if not isinstance(ativo, bool):
                raise ValidationError("ativo deve ser boolean", details={"field": "ativo"})
            setor.ativo = ativo

        return {"id": setor.id, "nome": setor.nome, "descricao": setor.descricao, "ativo": setor.ativo}