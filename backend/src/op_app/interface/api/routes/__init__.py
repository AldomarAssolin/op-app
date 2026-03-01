from .health_routes import bp_health
from .operador_routes import bp_operadores
from .setor_routes import bp_setores


def init_api(app):
    app.register_blueprint(bp_health)
    app.register_blueprint(bp_operadores)
    app.register_blueprint(bp_setores)