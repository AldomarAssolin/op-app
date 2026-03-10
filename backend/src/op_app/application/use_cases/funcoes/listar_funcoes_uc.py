class ListarFuncoesUC:
    def execute(self, uow) -> list:
        funcoes = uow.funcoes.list_all()
        return [{"id": funcao.id, "nome": funcao.nome_funcao} for funcao in funcoes]