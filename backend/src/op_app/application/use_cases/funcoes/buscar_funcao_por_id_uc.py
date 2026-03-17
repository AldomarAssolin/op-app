from src.op_app.application.errors import NotFoundError
from src.op_app.interface.api.schemas.funcao_dto import FuncaoDTO

class BuscarFuncaoPorIdUC:
    def execute(self, uow, funcao_id: int) -> FuncaoDTO:
        funcao = uow.funcoes.get_by_id(funcao_id)
        if not funcao:
            raise NotFoundError("Função não encontrada", details={"funcao_id": funcao_id})
        return FuncaoDTO(id=funcao.id, nome_funcao=funcao.nome_funcao)