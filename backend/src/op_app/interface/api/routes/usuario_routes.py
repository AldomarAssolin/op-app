from flask import Blueprint, request, jsonify

from src.op_app.infrastructure.uow.uow_sqlalchemy import UnitOfWorkSQLAlchemy
from src.op_app.application.use_cases.usuario.criar_usuario_uc import (
    CriarUsuarioUC,
    CriarUsuarioInput,
)
from src.op_app.application.use_cases.usuario.listar_usuario_uc import ListarUsuarioUC
from src.op_app.application.use_cases.usuario.buscar_usuario_por_id_uc import BuscarUsuarioPorIdUC
from src.op_app.application.use_cases.usuario.atualizar_usuario_parcial_uc import AtualizarUsuarioParcialUC
from src.op_app.application.use_cases.usuario.deletar_usuario_uc import DeletarUsuarioUC
from src.op_app.application.errors import NotFoundError, ValidationError

bp_usuarios = Blueprint("usuarios", __name__, url_prefix="/usuarios")


@bp_usuarios.post("")
def criar_usuario():
    payload = request.get_json(silent=True)

    if payload is None:
        raise ValidationError(
            "JSON inválido ou ausente",
            details={"hint": "Envie Content-Type: application/json e um body JSON válido"},
        )

    try:
        inp = CriarUsuarioInput(**payload)
    except TypeError as e:
        raise ValidationError(
            "Payload inválido",
            details={
                "hint": "Campos obrigatórios: nome, pin_hash, funcao, setor_id",
                "raw_error": str(e),
            },
        )

    with UnitOfWorkSQLAlchemy() as uow:
        result = CriarUsuarioUC().execute(uow, inp)

    return jsonify(result), 201


@bp_usuarios.get("")
def listar_usuarios():
    with UnitOfWorkSQLAlchemy() as uow:
        result = ListarUsuarioUC().execute(uow)
    return jsonify(result), 200


@bp_usuarios.get("/<int:usuario_id>")
def buscar_usuario_por_id(usuario_id: int):
    with UnitOfWorkSQLAlchemy() as uow:
        result = BuscarUsuarioPorIdUC().execute(uow, usuario_id)

    if not result:
        raise NotFoundError("Usuario não encontrado", details={"Usuario_id": usuario_id})

    return jsonify(result), 200


@bp_usuarios.patch("/<int:usuario_id>")
def atualizar_usuario_parcial(usuario_id: int):
    payload = request.get_json(silent=True)

    if payload is None:
        raise ValidationError(
            "JSON inválido ou ausente",
            details={"hint": "Envie Content-Type: application/json e um body JSON válido"},
        )

    if not payload:
        raise ValidationError(
            "Nenhum campo enviado",
            details={"hint": "Envie ao menos um campo para atualização via PATCH"},
        )

    with UnitOfWorkSQLAlchemy() as uow:
        result = AtualizarUsuarioParcialUC().execute(uow, usuario_id, payload)

    if not result:
        raise NotFoundError("Usuario não encontrado", details={"Usuario_id": usuario_id})

    return jsonify(result), 200


@bp_usuarios.delete("/<int:usuario_id>")
def deletar_usuario(usuario_id: int):
    with UnitOfWorkSQLAlchemy() as uow:
        ok = DeletarUsuarioUC().execute(uow, usuario_id)

    if not ok:
        raise NotFoundError("Usuario não encontrado", details={"Usuario_id": usuario_id})
        
    return ("", 204)