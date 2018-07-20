#dto.py
from flask_restplus import Namespace, fields

class EntryDto(object):
    """
    The Entry Data Transfer Object
    """
    api = Namespace('entries', description='Operations related to entries')
    entry = api.model('entries', {
        'id': fields.String(readonly=True),
        'title': fields.String(required=True, description='The title for the journal entry'),
        'content': fields.String(required=True, description='The content for the journal entry')
    })

class UserDto(object):
    """
    The User Data Transfer Object
    """
    auth = Namespace('auth', description='Operations related to users')
    user = auth.model('user', {
        'id': fields.String(description='User Identifier'),
        'username': fields.String(required=True, description='User username'),
        'email': fields.String(required=True, description='User email address'),        
        'password': fields.String(required=True, description='User password')
    })
    