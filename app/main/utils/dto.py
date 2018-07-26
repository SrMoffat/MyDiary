#dto.py
from flask_restplus import Namespace, fields

class EntryDto(object):
    """
    The Entry Data Transfer Object
    """
    api = Namespace('entries', description='Operations related to entries')
    entry_model = api.model('Entries', {        
        'title': fields.String(required=True, description='The title for the journal entry', example="My Day on the Moon"),
        'content': fields.String(required=True, description='The content for the journal entry', example="Rivers, shivers, dealers, triggers")
    })

class UserDto(object):
    """
    The User Data Transfer Object
    """
    auth = Namespace('auth', description='Operations related to the users')
    signup_model = auth.model('Registration', {        
        'username': fields.String(required=True, description='Enter username', example="4fr0c0d3"),
        'email': fields.String(required=True, description='Enter email', example="4fr0c0d3@mail.com"),
        'password': fields.String(required=True, description='Password', example="d4rk4ng3l")
    })
    login_model = auth.model('Log In', {        
        'username': fields.String(required=True, description='Enter username', example="4fr0c0d3"),
        'password': fields.String(required=True, description='Password', example="d4rk4ng3l")
    })
    