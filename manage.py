#manage.py 
import unittest
from flask_script import Manager

from app import blueprint
from app.main import create_app, app_configs


app = create_app('test')
app.register_blueprint(blueprint)

manager = Manager(app)

@manager.command
def run(): 
    app.run()

@manager.command
def test(): 
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)   


if __name__ == '__main__': 
    manager.run()


