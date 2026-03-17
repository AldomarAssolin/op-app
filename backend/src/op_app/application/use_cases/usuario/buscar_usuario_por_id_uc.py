from typing import Optional

from src.op_app.application.errors import ValidationError
from src.op_app.interface.api.schemas.usuario_dto import UsuarioDTO


class BuscarUsuarioPorIdUC:
    def execute(self, uow, usuarios_id: int) -> Optional[UsuarioDTO]:
        usuarios = uow.usuarios.get_by_id(usuarios_id)

        if not usuarios:
            return None

        return UsuarioDTO(
            id=usuarios.id,
            nome=usuarios.nome,
            pin=usuarios.pin,
            funcao_id=usuarios.funcao_id,
            setor_id=usuarios.setor_id,
        )