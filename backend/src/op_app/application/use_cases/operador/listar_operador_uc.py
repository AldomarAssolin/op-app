from typing import List, Dict, Any

  
class ListarOperadoresUC:
    def execute(self, uow) -> List[Dict[str, Any]]:
        operadores = uow.operadores.list_all()
        
        return [
            {"id": o.id, "nome": o.nome, "funcao": o.funcao, "setor": o.setor}
            for o in operadores
        ]