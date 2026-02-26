from flask import Flask
from src.op_app.interface.api.routes.health_routes import bp_health
from src.op_app.interface.api.routes.operador_routes import bp_operadores
from src.op_app.infrastructure.db.session import init_session, remove_session

def create_app() -> Flask:
    app = Flask(__name__)

    # Inicializa DB/session aqui (uma vez por processo)
    init_session()

    app.register_blueprint(bp_health)
    app.register_blueprint(bp_operadores)

    # Remove sessão ao final de cada request
    @app.teardown_appcontext
    def cleanup(exception=None):
        remove_session()

    return app