from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config(object):
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('TRACK')
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class HomologConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'homolog': HomologConfig,
    'default': DevelopmentConfig,
    'production': ProductionConfig
}
