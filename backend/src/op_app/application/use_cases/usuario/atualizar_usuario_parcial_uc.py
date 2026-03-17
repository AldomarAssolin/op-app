from typing import Dict, Any, Optional

from src.op_app.application.errors import ValidationError
from src.op_app.interface.api.schemas.usuario_dto import UsuarioDTO


class AtualizarUsuarioParcialUC:
    def execute(self, uow, usuario_id: int, data: Dict[str, Any]) -> Optional[UsuarioDTO]:
        usuario = uow.usuarios.get_by_id(usuario_id)

        if not usuario:
            return None

        # Atualiza somente campos enviados
        for campo in ("nome", "pin_hash", "funcao_id", "setor_id"):
            if campo in data:
                valor = (data[campo] or "")
                if not valor:
                    raise ValidationError(
                        f"Campo '{campo}' não pode ser vazio",
                        details={"field": campo},
                    )
                setattr(usuario, campo, valor)

        return UsuarioDTO(
            id=usuario.id,
            nome=usuario.nome.strip(),
            pin_hash=usuario.pin_hash,
            funcao_id=usuario.funcao_id,
            setor_id=usuario.setor_id,
        )