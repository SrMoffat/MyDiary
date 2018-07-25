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
    auth = Namespace('auth', description='Operations related to the users')
    user = auth.model('users', {
        'id': fields.String(readonly=True),
        'username': fields.String(required=True, description='The username for the user'),
        'email': fields.String(required=True, description='The email for the suer'),
        'password': fields.String(required=True, description='The password for the suer')
    })
    