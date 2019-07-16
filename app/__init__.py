from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import app_config
from flasgger import Swagger


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Informe suas Credenciais!'

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config['SWAGGER'] = {
        'title': 'STARTER API',
        'version': '1.0.0',
        'uiversion': 3,
        "specs_route": "/api/docs"
    }
    CORS(app)
    Swagger(app)
    db.init_app(app)
    from .dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    login_manager.init_app(app)
    return app
