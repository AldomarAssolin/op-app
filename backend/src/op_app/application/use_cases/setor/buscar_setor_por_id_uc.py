from src.op_app.application.errors import NotFoundError
from src.op_app.interface.api.schemas.setor_dto import SetorDTO


class BuscarSetorPorIdUC:
    def execute(self, uow, setor_id: int) -> SetorDTO:
        setor = uow.setores.get_by_id(setor_id)
        if not setor:
            raise NotFoundError("Setor não encontrado", details={"setor_id": setor_id})
        return SetorDTO(
            id=setor.id,
            nome=setor.nome,
            codigo_setor=setor.codigo_setor,
            ativo=setor.ativo,
        )