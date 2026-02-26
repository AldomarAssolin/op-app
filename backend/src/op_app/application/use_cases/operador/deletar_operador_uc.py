class DeletarOperadorUC:
    def execute(self, uow, operador_id: int) -> bool:
        return uow.operadores.delete_by_id(operador_id)