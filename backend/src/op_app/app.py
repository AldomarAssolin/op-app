from flask import Flask
import logging
from src.op_app.interface.api.routes.health_routes import bp_health
from src.op_app.interface.api.routes.usuario_routes import bp_usuarios
from src.op_app.interface.api.routes.setor_routes import bp_setores
from src.op_app.interface.api.routes.funcao_routes import bp_funcoes

from src.op_app.infrastructure.db.session import init_session, remove_session
from src.op_app.interface.api.error_handlers import register_error_handlers

def configure_logging():
    # Aqui a gente define o "esquadro" do log
    logging.basicConfig(
        level=logging.INFO,  # Define que queremos ver do nível INFO para cima
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler() # Manda para o terminal (console)
            # logging.FileHandler("app.log") # Se quiser salvar num arquivo depois
        ]
    )

def create_app() -> Flask:
    """Factory para criar a aplicação Flask, configurar rotas, banco e logging.
    
        - Essa função é chamada pelo Gunicorn para criar a instância da aplicação.
        - O logging é configurado aqui para garantir que seja inicializado antes de qualquer outra coisa.
        - Assim, qualquer log gerado durante a inicialização do app ou das rotas já estará formatado e visível.
        
    """
    configure_logging()
    logger = logging.getLogger(__name__)
    app = Flask(__name__)
    
    logger.info(">>> PASSO 1: Logging OK")
    # Handlers globais de erro (padroniza JSON)
    register_error_handlers(app)
    logger.info(">>> PASSO 2: Error Handlers OK")

    logger.info(">>> PASSO 3: Tentando init_session()...")
    # Inicializa DB/session aqui (uma vez por processo)
    init_session() 
    logger.info(">>> PASSO 4: init_session() FINALIZADO")

    # Blueprints
    logger.info(">>> PASSO 5: Registrando Blueprints...")
    app.register_blueprint(bp_health)
    app.register_blueprint(bp_usuarios)
    app.register_blueprint(bp_setores)
    app.register_blueprint(bp_funcoes)
    
    # Remove sessão ao final de cada request
    @app.teardown_appcontext
    def cleanup(exception=None):
        remove_session()
    
    logger.info(">>> PASSO 6: TUDO PRONTO!")
    return app

