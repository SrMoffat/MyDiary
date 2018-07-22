#manage.py
import os
from flask_script import Manager

from app import blueprint
from app.main import create_app

app = create_app(config_name=os.getenv("APP_CONFIG"))
app.register_blueprint(blueprint)
manager = Manager(app)

@manager.command
def run(): 
    app.run()

if __name__ == '__main__': 
    manager.run()
