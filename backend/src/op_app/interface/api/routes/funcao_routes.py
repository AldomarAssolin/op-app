from flask import Blueprint, request, jsonify

from src.op_app.infrastructure.uow.uow_sqlalchemy import UnitOfWorkSQLAlchemy
from src.op_app.application.errors import ValidationError
from src.op_app.application.use_cases.funcoes.criar_funcao_uc import CriarFuncaoUC, CriarFuncaoInput
from src.op_app.application.use_cases.funcoes.listar_funcoes_uc import ListarFuncoesUC
from src.op_app.application.use_cases.funcoes.buscar_funcao_por_id_uc import BuscarFuncaoPorIdUC
from src.op_app.application.use_cases.funcoes.atualizar_funcao_uc import AtualizarFuncaoUC
from src.op_app.application.use_cases.funcoes.deletar_funcao_uc import DeletarFuncaoUC

bp_funcoes = Blueprint("funcoes", __name__, url_prefix="/funcoes")

@bp_funcoes.get("/test")
def teste():
    return jsonify({"message": "API de funções funcionando!"}), 200

@bp_funcoes.post("")
def criar_funcao():
    payload = request.get_json(silent=True)
    if payload is None:
        raise ValidationError("JSON inválido ou ausente")

    try:
        inp = CriarFuncaoInput(**payload)
    except TypeError as e:
        raise ValidationError("Payload inválido", details={"raw_error": str(e), "fields": ["nome_funcao"]})

    with UnitOfWorkSQLAlchemy() as uow:
        result = CriarFuncaoUC().execute(uow, inp)

    return jsonify(result), 201

@bp_funcoes.get("")
def listar_funcoes():
    with UnitOfWorkSQLAlchemy() as uow:
        result = ListarFuncoesUC().execute(uow)
    return jsonify(result), 200

@bp_funcoes.get("/<int:funcao_id>")
def buscar_funcao_por_id(funcao_id: int):
    with UnitOfWorkSQLAlchemy() as uow:
        result = BuscarFuncaoPorIdUC().execute(uow, funcao_id)
    return jsonify(result), 200

@bp_funcoes.patch("/<int:funcao_id>")
def atualizar_funcao_parcial(funcao_id: int):
    payload = request.get_json(silent=True)
    if payload is None:
        raise ValidationError("JSON inválido ou ausente")
    if not payload:
        raise ValidationError("Nenhum campo enviado")

    with UnitOfWorkSQLAlchemy() as uow:
        result = AtualizarFuncaoUC().execute(uow, funcao_id, payload)

    return jsonify(result), 200

@bp_funcoes.delete("/<int:funcao_id>")
def deletar_funcao(funcao_id: int):
    with UnitOfWorkSQLAlchemy() as uow:
        success = DeletarFuncaoUC().execute(uow, funcao_id)

    if not success:
        return jsonify({"message": "Função não encontrada"}), 404

    return jsonify({"message": "Função deletada com sucesso"}), 200

