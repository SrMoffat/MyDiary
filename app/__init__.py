#app __init__.py
from flask_restplus import Api
from flask import Blueprint

from .main.controller.auth_controller import auth as auth_ns
from .main.controller.entry_controller import api as entries_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          version='1.0',
          title='MyDiary RESTful API',
          description='A RESTful API built on Flask')

del api.namespaces[0]

api.add_namespace(auth_ns, path='/api/v2/auth')
api.add_namespace(entries_ns, path='/api/v2')
