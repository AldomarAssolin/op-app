from flask import Flask
#from src.config import DevConfig
from src.op_app.interface.api.routes.health_routes import bp_health

def create_app() -> Flask:
    app = Flask(__name__)
    #app.config.from_object(config_class)
    
    # Registrar blueprints
    app.register_blueprint(bp_health)
    
    return app