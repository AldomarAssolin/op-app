from flask import Flask
from src.op_app.interface.api.routes.health_routes import bp_health
from src.op_app.interface.api.routes.usuario_routes import bp_usuarios
from src.op_app.interface.api.routes.setor_routes import bp_setores
from src.op_app.interface.api.routes.funcao_routes import bp_funcoes

from src.op_app.infrastructure.db.session import init_session, remove_session
from src.op_app.interface.api.error_handlers import register_error_handlers

def create_app() -> Flask:
    app = Flask(__name__)
    
    # Handlers globais de erro (padroniza JSON)
    register_error_handlers(app)

    # Inicializa DB/session aqui (uma vez por processo)
    init_session()

    # Blueprints
    app.register_blueprint(bp_health)
    app.register_blueprint(bp_usuarios)
    app.register_blueprint(bp_setores)
    app.register_blueprint(bp_funcoes)

    # Remove sessão ao final de cada request
    @app.teardown_appcontext
    def cleanup(exception=None):
        remove_session()

    return app