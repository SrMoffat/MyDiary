#app __init__.py
from flask_restplus import Api
from flask import Blueprint

from .main.controller.entry_controller import api as entry_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          version='1.0',
          title='MyDiary RESTful API',
          description='A RESTful API built on Flask')

api.add_namespace(entry_ns, path='/api/v1')
