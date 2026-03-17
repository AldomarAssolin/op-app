from typing import List
from src.op_app.interface.api.schemas.funcao_dto import FuncaoDTO

class ListarFuncoesUC:
    def execute(self, uow) -> List[FuncaoDTO]:
        funcoes = uow.funcoes.list_all()
        return [FuncaoDTO(id=funcao.id, nome_funcao=funcao.nome_funcao) for funcao in funcoes]