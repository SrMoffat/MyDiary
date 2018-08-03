#main __init__.py
import os

from flask import Flask, jsonify

from .config import app_configs

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_configs[os.getenv('APP_CONFIG')])
    
    @app.errorhandler(404)
    def error_404(error):
        return jsonify({"error":"Page Not Found!"})
    @app.errorhandler(500)
    def error_500(error):
        return jsonify({"error":"Something went wrong!"})
    return app
    