#dto.py
from flask_restplus import Namespace, fields

class EntryDto(object):
    """
    The Entry Data Transfer Object
    """
    api = Namespace('entries', description='Operations related to entries')
    entry = api.model('entries', {
        'title': fields.String(required=True, description='The title for the journal entry'),
        'content': fields.String(required=True, description='The content for the journal entry')
    })