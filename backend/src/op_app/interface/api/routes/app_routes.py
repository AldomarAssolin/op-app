from flask import Blueprint, jsonify

bp_app = Blueprint('app', __name__)

@bp_app.route('/', methods=['GET'])
def index():
    return {
        "service": "op-app",
        "status": "running",
        "endpoints": [
            "/health",
            "/usuarios",
            "/setores",
            "/funcoes"
        ]
    }