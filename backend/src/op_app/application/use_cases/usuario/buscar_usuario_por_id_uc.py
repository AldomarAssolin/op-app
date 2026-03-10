from typing import Dict, Any

from src.op_app.application.errors import ValidationError


class BuscarUsuarioPorIdUC:
    def execute(self, uow, usuarios_id: int) -> Dict[str, Any] | None:
        usuarios = uow.usuarios.get_by_id(usuarios_id)

        if not usuarios:
            return None

        return {
            "id": usuarios.id,
            "nome": usuarios.nome,
            "funcao": usuarios.funcao_id,
            "setor": usuarios.setor_id,
        }