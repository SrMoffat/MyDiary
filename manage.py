"""
The manage module is the entry for the app
"""
import os
from flask_script import Manager

from app import blueprint
from app.main import create_app

app = create_app(config_name=os.getenv("APP_CONFIG"))
app.register_blueprint(blueprint)
manager = Manager(app)

@manager.command
def run():
    """
    RUN the application
    """
    app.run()

if __name__ == '__main__':
    manager.run()
