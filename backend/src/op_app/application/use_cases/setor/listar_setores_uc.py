class ListarSetoresUC:
    def execute(self, uow) -> list[dict]:
        setores = uow.setores.list_all()
        
        if not setores:
            return []
        
        return [{"id": s.id, "nome": s.nome, "codigo_setor": s.codigo_setor, "ativo": s.ativo} for s in setores]