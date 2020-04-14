import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'DobryTajemyKlucz02!!!'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    INPAINT_API_URL = os.environ.get('DEV_INPAINT_API_URL')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class ProductionConfig(Config):
    DEBUG = False
    INPAINT_API_URL = os.environ.get('INPAINT_API_URL')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
