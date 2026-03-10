from src.op_app.application.errors import NotFoundError

class DeletarFuncaoUC:
    def execute(self, uow, funcao_id: int) -> None:
        funcao = uow.funcoes.get_by_id(funcao_id)
        if not funcao:
            raise NotFoundError("Função não encontrada", details={"funcao_id": funcao_id})
        
        uow.funcoes.delete(funcao_id)
        return True