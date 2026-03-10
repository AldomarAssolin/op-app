from .health_routes import bp_health
from .usuario_routes import bp_usuarios
from .funcao_routes import bp_funcoes
from .setor_routes import bp_setores


def init_api(app):
    app.register_blueprint(bp_health)
    app.register_blueprint(bp_usuarios)
    app.register_blueprint(bp_setores)
    app.register_blueprint(bp_funcoes)