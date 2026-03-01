from flask import Blueprint, request, jsonify
from src.op_app.infrastructure.db.models.operador_model import OperadorModel
from src.op_app.infrastructure.uow.uow_sqlalchemy import UnitOfWorkSQLAlchemy
from src.op_app.application.use_cases.operador.criar_operador_uc import CriarOperadorUC, CriarOperadorInput
from src.op_app.application.use_cases.operador.listar_operador_uc import ListarOperadoresUC
from src.op_app.application.use_cases.operador.buscar_operador_por_id_uc import BuscarOperadorPorIdUC
from src.op_app.application.use_cases.operador.atualizar_operador_parcial_uc import AtualizarOperadorParcialUC
from src.op_app.application.use_cases.operador.deletar_operador_uc import DeletarOperadorUC
from src.op_app.application.errors import NotFoundError
from src.op_app.application.errors import ValidationError

bp_operadores = Blueprint("operadores", __name__, url_prefix="/operadores")

@bp_operadores.post("")
def criar_operador():
    payload = request.get_json(silent=True)

    if payload is None:
        raise ValidationError(
            "JSON inválido ou ausente",
            details={"hint": "Envie Content-Type: application/json e um body JSON válido"}
        )

    try:
        inp = CriarOperadorInput(**payload)
    except TypeError as e:
        # faltou campo obrigatório ou veio chave errada
        raise ValidationError(
            "Payload inválido",
            details={"hint": "Campos obrigatórios: nome, funcao, setor", "raw_error": str(e)}
        )

    with UnitOfWorkSQLAlchemy() as uow:
        result = CriarOperadorUC().execute(uow, inp)

    return jsonify(result), 201
    
@bp_operadores.get("")
def listar_operadores():
    with UnitOfWorkSQLAlchemy() as uow:
        result = ListarOperadoresUC().execute(uow)
    return jsonify(result), 200
    
@bp_operadores.get("/<int:operador_id>")
def buscar_operador_por_id(operador_id: int):
    with UnitOfWorkSQLAlchemy() as uow:
        result = BuscarOperadorPorIdUC().execute(uow, operador_id)

    if not result:
        return NotFoundError("OPerador não encontrado", details={"operador_id": operador_id})

    return jsonify(result), 200

@bp_operadores.patch("/<int:operador_id>")
def atualizar_operador_parcial(operador_id: int):
    payload = request.get_json(silent=True) or {}

    if not payload:
        return jsonify({"error": "Nenhum campo enviado"}), 400

    try:
        with UnitOfWorkSQLAlchemy() as uow:
            result = AtualizarOperadorParcialUC().execute(uow, operador_id, payload)

        if not result:
            return jsonify({"error": "Operador não encontrado"}), 404

        return jsonify(result), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@bp_operadores.delete("/<int:operador_id>")
def deletar_operador(operador_id: int):
    with UnitOfWorkSQLAlchemy() as uow:
        ok = DeletarOperadorUC().execute(uow, operador_id)

    if not ok:
        return jsonify({"error": "Operador não encontrado"}), 404

    return ("", 204)
