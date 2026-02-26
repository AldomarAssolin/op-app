from flask import Blueprint, request, jsonify
from src.op_app.infrastructure.db.models.operador_model import OperadorModel
from src.op_app.infrastructure.uow.uow_sqlalchemy import UnitOfWorkSQLAlchemy

bp_operadores = Blueprint("operadores", __name__, url_prefix="/operadores")

# Rota teste
@bp_operadores.get("/test")
def teste_operadores():
    return jsonify([
        {
        "Teste":"Testando rota",
        "status":"Rota OK"
        }
    ]), 200

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
    
@bp_operadores.get("")
def listar_operadores():
    with UnitOfWorkSQLAlchemy() as uow:
        operadores = uow.operadores.list_all()

    return jsonify([
        {"id": o.id, "nome": o.nome, "funcao": o.funcao, "setor": o.setor}
        for o in operadores
    ]), 200
    
@bp_operadores.get("/<int:operador_id>")
def buscar_operador_por_id(operador_id):
    with UnitOfWorkSQLAlchemy() as uow:
        operador = uow.operadores.get_by_id(operador_id)
        
    if not operador:
        return {"message": "Operador não encontrado"}, 404
        
    return jsonify([
        {"id": operador.id, "nome": operador.nome, "funcao": operador.funcao, "setor": operador.setor}
    ]), 200

@bp_operadores.patch("/<int:operador_id>")
def atualizar_operador(operador_id):
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Body vazio"}), 400

    nome = data.get("nome")
    funcao = data.get("funcao")
    setor = data.get("setor")

    if not nome or not funcao or not setor:
        return jsonify({"error": "Campos obrigatórios: nome, funcao, setor"}), 400

    with UnitOfWorkSQLAlchemy() as uow:
        existing = uow.operadores.get_by_id(operador_id)
        if not existing:
            return jsonify({"error": "Operador não encontrado"}), 404

        existing.nome = nome
        existing.funcao = funcao
        existing.setor = setor

        # monta resposta aqui, ainda com session viva
        payload = {
            "id": existing.id,
            "nome": existing.nome,
            "funcao": existing.funcao,
            "setor": existing.setor
        }

    return jsonify(payload), 200

    
    

    