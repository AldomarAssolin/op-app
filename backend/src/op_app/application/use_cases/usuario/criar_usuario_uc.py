from dataclasses import dataclass

from src.op_app.infrastructure.db.models.usuario_model import UsuarioModel
from src.op_app.application.errors import ValidationError, NotFoundError

@dataclass(frozen=True)
class CriarUsuarioInput:
    nome: str
    pin: str
    funcao_id: str
    setor_id: int


class CriarUsuarioUC:
    def execute(self, uow, data: CriarUsuarioInput) -> dict:
        nome = (data.nome or "").strip()
        pin = (data.pin or "").strip()
        funcao_id = data.funcao_id
        setor_id = data.setor_id 

    
        # setor_id pode vir como int, mas às vezes chega string no JSON
        try:
            setor_id = int(data.setor_id)
        except (TypeError, ValueError):
            raise ValidationError(
                "setor_id inválido",
                details={"field": "setor_id", "hint": "Envie um inteiro válido"},
            )
            
        try:
            funcao_id = int(data.funcao_id)
        except (TypeError, ValueError):
            raise ValidationError(
                "funcao_id inválido",
                details={"field": "funcao_id", "hint": "Envie um inteiro válido"},
            )

        if not nome or not pin:
            raise ValidationError(
                "Campos obrigatórios: nome, pin",
                details={"fields": ["nome", "pin", "funcao_id", "setor_id"]},
            )


        setor = uow.setores.get_by_id(setor_id) 
        funcao = uow.funcoes.get_by_id(funcao_id)
        
        if not setor:
            raise NotFoundError("Setor não encontrado", details={"setor_id": setor_id})
        
        if not funcao:
            raise NotFoundError("Função não encontrada", details={"funcao_id": funcao_id})

        # Chamando o construtor do modelo em vez da entidade de domínio
        usuarios = UsuarioModel(nome=nome, pin=pin, funcao_id=funcao_id, setor_id=setor_id) 
        usuarios = uow.usuarios.add(usuarios) 

        return {
            "id": usuarios.id,
            "nome": usuarios.nome,
            "pin": usuarios.pin,
            "funcao_id": usuarios.funcao_id,
            "setor_id": usuarios.setor_id,
        }