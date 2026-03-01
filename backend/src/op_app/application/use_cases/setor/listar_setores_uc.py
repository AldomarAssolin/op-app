class ListarSetoresUC:
    def execute(self, uow) -> list[dict]:
        setores = uow.setores.list_all()
        return [{"id": s.id, "nome": s.nome, "descricao": s.descricao, "ativo": s.ativo} for s in setores]