from src.op_app.application.errors import NotFoundError

class DeletarSetorUC:
    def execute(self, uow, setor_id: int) -> bool:
        setor = uow.setores.get_by_id(setor_id)
        
        
        if not setor:
            raise NotFoundError("Setor não encontrado", details={"setor_id": setor_id})

        uow.setores.delete_by_id(setor_id)
        return True