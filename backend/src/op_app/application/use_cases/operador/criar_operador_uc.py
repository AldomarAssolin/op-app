from dataclasses import dataclass

from src.op_app.infrastructure.db.models.operador_model import OperadorModel

@dataclass(frozen=True)
class CriarOperadorInput:
    nome:str
    funcao: str
    setor:str
    
class CriarOperadorUC:
    def execute(self, uow, data: CriarOperadorInput) -> dict:
        nome = (data.nome or "").strip()
        funcao = (data.funcao or "").strip()
        setor = (data.setor or "").strip()
        
        if not nome or not funcao or not setor:
            raise ValueError("Campos obrigatorios: nome, funcao, setor")
        
        operador = OperadorModel(nome=nome, funcao=funcao, setor=setor)
        uow.operadores.add(operador)
        
        return {
            "id": operador.id,
            "nome": operador.nome,
            "funcao": operador.funcao,
            "setor": operador.setor,
        }