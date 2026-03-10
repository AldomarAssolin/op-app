from src.op_app.application.errors import NotFoundError

class BuscarSetorPorIdUC:
    def execute(self, uow, setor_id: int) -> dict:
        setor = uow.setores.get_by_id(setor_id)
        if not setor:
            raise NotFoundError("Setor não encontrado", details={"setor_id": setor_id})
        return {"id": setor.id, "nome": setor.nome, "codigo_setor": setor.codigo_setor, "ativo": setor.ativo}