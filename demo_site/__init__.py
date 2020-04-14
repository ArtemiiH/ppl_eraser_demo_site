import os

from flask import Flask

from .config import configs


def create_app(config_name: str = 'development', config_dict: dict = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    if config_dict:
        app.config.from_mapping(config_dict)
    elif config_name:
        print(config_name)
        app.config.from_object(configs[config_name])
        configs[config_name].init_app(app)

    from .routes import bp
    app.register_blueprint(bp, url_prefix='/')

    return app
