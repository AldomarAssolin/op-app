from flask import Blueprint, request, jsonify
from src.op_app.infrastructure.db.models.operador_model import OperadorModel
from src.op_app.infrastructure.uow.uow_sqlalchemy import UnitOfWorkSQLAlchemy

bp_operadores = Blueprint("operadores", __name__, url_prefix="/operadores")


@bp_operadores.post("")
def criar_operador():
    data = request.get_json()

    # Validação simples
    if not data:
        return jsonify({"error": "Body vazio"}), 400

    nome = data.get("nome")
    funcao = data.get("funcao")
    setor = data.get("setor")

    if not nome or not funcao or not setor:
        return jsonify({"error": "Campos obrigatórios: nome, funcao, setor"}), 400

    with UnitOfWorkSQLAlchemy() as uow:
        operador = OperadorModel(
            nome=nome,
            funcao=funcao,
            setor=setor,
        )
        uow.operadores.add(operador)

    return jsonify({
        "id": operador.id,
        "nome": operador.nome,
        "funcao": operador.funcao,
        "setor": operador.setor
    }), 201