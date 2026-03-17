from typing import List

from src.op_app.interface.api.schemas.usuario_dto import UsuarioDTO


class ListarUsuarioUC:
    def execute(self, uow) -> List[UsuarioDTO]:
        usuarios = uow.usuarios.list_all()

        return [
            UsuarioDTO(
                id=u.id,
                nome=u.nome,
                pin=u.pin,
                funcao_id=u.funcao_id,
                setor_id=u.setor_id,
            )
            for u in usuarios
        ]