from flask import jsonify
from src.op_app.application.errors import AppError

def register_error_handlers(app):
    @app.errorhandler(AppError)
    def handle_app_error(err: AppError):
        return jsonify({
            "error": {
                "code": err.code,
                "message": err.message,
                "details": err.details
            }
        }), err.status_code

    @app.errorhandler(Exception)
    def handle_unexpected_error(err: Exception):
        # em produção, não vaza stacktrace pro cliente
        return jsonify({
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "Erro interno do servidor",
                "details": {}
            }
        }), 500