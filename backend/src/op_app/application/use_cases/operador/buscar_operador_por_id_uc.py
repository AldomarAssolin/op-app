from typing import Dict, Any


class BuscarOperadorPorIdUC:
    def execute(self, uow, operador_id: int) -> Dict[str, Any] | None:
        operador = uow.operadores.get_by_id(operador_id)

        if not operador:
            return None

        return {
            "id": operador.id,
            "nome": operador.nome,
            "funcao": operador.funcao,
            "setor": operador.setor,
        }