from src.op_app.application.errors import NotFoundError

class BuscarFuncaoPorIdUC:
    def execute(self, uow, funcao_id: int) -> dict:
        funcao = uow.funcoes.get_by_id(funcao_id)
        if not funcao:
            raise NotFoundError("Função não encontrada", details={"funcao_id": funcao_id})
        return {"id": funcao.id, "nome": funcao.nome_funcao}