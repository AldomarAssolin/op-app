from src.op_app.application.errors import ValidationError, NotFoundError, ConflictError

class AtualizarFuncaoUC:
    def execute(self, uow, funcao_id: int, payload: dict) -> dict:
        funcao = uow.funcoes.get_by_id(funcao_id)

        if not funcao:
            raise NotFoundError("Função não encontrada", details={"funcao_id": funcao_id})

        if "nome_funcao" in payload:
            nome = (payload.get("nome_funcao") or "").strip()
            
            if not nome:
                raise ValidationError("nome não pode ser vazio", details={"field": "nome"})

            existente = uow.funcoes.get_by_nome(nome)
            if existente and existente.id != funcao_id:
                raise ConflictError("Já existe uma função com esse nome", details={"nome": nome})

            funcao.nome_funcao = nome

        return {"id": funcao.id, "nome": funcao.nome_funcao}