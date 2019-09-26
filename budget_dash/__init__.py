import os

from flask import Flask

from config import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    from .api.routes import api

    app.register_blueprint(api)

    return app
