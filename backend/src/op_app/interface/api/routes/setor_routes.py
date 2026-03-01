from flask import Blueprint, request, jsonify

from src.op_app.infrastructure.uow.uow_sqlalchemy import UnitOfWorkSQLAlchemy
from src.op_app.application.errors import ValidationError
from src.op_app.application.use_cases.setor.criar_setor_uc import CriarSetorUC, CriarSetorInput
from src.op_app.application.use_cases.setor.listar_setores_uc import ListarSetoresUC
from src.op_app.application.use_cases.setor.buscar_setor_por_id_uc import BuscarSetorPorIdUC
from src.op_app.application.use_cases.setor.atualizar_setor_parcial_uc import AtualizarSetorParcialUC
from src.op_app.application.use_cases.setor.deletar_setor_uc import DeletarSetorUC

bp_setores = Blueprint("setores", __name__, url_prefix="/setores")


@bp_setores.get("/test")
def teste():
    return jsonify({"message": "API de setores funcionando!"}), 200

@bp_setores.post("")
def criar_setor():
    payload = request.get_json(silent=True)
    if payload is None:
        raise ValidationError("JSON inválido ou ausente")

    try:
        inp = CriarSetorInput(**payload)
    except TypeError as e:
        raise ValidationError("Payload inválido", details={"raw_error": str(e), "fields": ["nome"]})

    with UnitOfWorkSQLAlchemy() as uow:
        result = CriarSetorUC().execute(uow, inp)

    return jsonify(result), 201


@bp_setores.get("")
def listar_setores():
    with UnitOfWorkSQLAlchemy() as uow:
        result = ListarSetoresUC().execute(uow)
    return jsonify(result), 200


@bp_setores.get("/<int:setor_id>")
def buscar_setor_por_id(setor_id: int):
    with UnitOfWorkSQLAlchemy() as uow:
        result = BuscarSetorPorIdUC().execute(uow, setor_id)
    return jsonify(result), 200


@bp_setores.patch("/<int:setor_id>")
def atualizar_setor_parcial(setor_id: int):
    payload = request.get_json(silent=True)
    if payload is None:
        raise ValidationError("JSON inválido ou ausente")
    if not payload:
        raise ValidationError("Nenhum campo enviado")

    with UnitOfWorkSQLAlchemy() as uow:
        result = AtualizarSetorParcialUC().execute(uow, setor_id, payload)

    return jsonify(result), 200


@bp_setores.delete("/<int:setor_id>")
def deletar_setor(setor_id: int):
    with UnitOfWorkSQLAlchemy() as uow:
        DeletarSetorUC().execute(uow, setor_id)
    return ("", 204)