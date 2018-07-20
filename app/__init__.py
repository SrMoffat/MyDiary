#app __init__.py
from flask_restplus import Api
from flask import Blueprint

from .main.controller.entry_controller import api as entry_ns
from .main.controller.user_controller import auth as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          version='1.0',
          title='MyDiary RESTful API',
          description='A RESTful API built on Flask')

del api.namespaces[0] # Remove default namespace

api.add_namespace(entry_ns, path='/api/v1')
api.add_namespace(auth_ns, path='/api/v1/auth')
