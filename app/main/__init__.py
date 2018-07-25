#main __init__.py
import os
from flask import Flask 

from .config import app_configs

def create_app(config_name): 
    app = Flask(__name__)
    app.config.from_object(app_configs[os.getenv('APP_CONFIG')])

    return app
    