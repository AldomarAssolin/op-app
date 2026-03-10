from typing import List, Dict, Any

  
class ListarUsuarioUC:
    def execute(self, uow) -> List[Dict[str, Any]]:
        usuarios = uow.usuarios.list_all()
        
        return [
            {"id": u.id, "nome": u.nome, "funcao": u.funcao_id, "setor": u.setor_id}
            for u in usuarios
        ]