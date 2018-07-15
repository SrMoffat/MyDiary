#main __init__.py
from flask import Flask 

from .config import app_configs


def create_app(config_name): 
    app = Flask(__name__)
    app.config.from_object(app_configs[config_name])

    return app
    