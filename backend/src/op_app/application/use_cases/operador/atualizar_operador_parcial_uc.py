from typing import Dict, Any


class AtualizarOperadorParcialUC:
    def execute(self, uow, operador_id: int, data: Dict[str, Any]) -> Dict[str, Any] | None:
        operador = uow.operadores.get_by_id(operador_id)

        if not operador:
            return None

        # Atualiza somente campos enviados
        for campo in ("nome", "funcao", "setor"):
            if campo in data:
                valor = (data[campo] or "").strip()
                if not valor:
                    raise ValueError(f"Campo '{campo}' não pode ser vazio")
                setattr(operador, campo, valor)

        return {
            "id": operador.id,
            "nome": operador.nome,
            "funcao": operador.funcao,
            "setor": operador.setor,
        }