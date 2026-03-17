from typing import List

from src.op_app.interface.api.schemas.setor_dto import SetorDTO


class ListarSetoresUC:
    def execute(self, uow) -> List[SetorDTO]:
        setores = uow.setores.list_all()

        if not setores:
            return []

        return [
            SetorDTO(
                id=s.id,
                nome=s.nome,
                codigo_setor=s.codigo_setor,
                ativo=s.ativo,
            )
            for s in setores
        ]