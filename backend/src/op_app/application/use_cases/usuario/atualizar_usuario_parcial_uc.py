from typing import Dict, Any

from src.op_app.application.errors import ValidationError


class AtualizarUsuarioParcialUC:
    def execute(self, uow, usuario_id: int, data: Dict[str, Any]) -> Dict[str, Any] | None:
        usuario = uow.usuarios.get_by_id(usuario_id)

        if not usuario:
            return None

        # Atualiza somente campos enviados
        for campo in ("nome", "funcao_id", "setor_id"):
            if campo in data:
                valor = (data[campo] or "")
                if not valor:
                    raise ValueError(f"Campo '{campo}' não pode ser vazio", details={"Field": campo})
                setattr(usuario, campo, valor)

        return {
            "id": usuario.id,
            "nome": usuario.nome.strip(),
            "funcao_id": usuario.funcao_id,
            "setor_id": usuario.setor_id,
        }