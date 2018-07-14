#entry_controller.py
from flask import request 
from flask_restplus import Resource

from ..utils.dto import EntryDto
from ..service.entry_service import add_entry

api = EntryDto.api
entry = EntryDto.entry

@api.route('/entries')        
class Entries(Resource):
    """
    The Entry Resource for the API
    """
    @api.expect(entry, validate=True)
    @api.response(201, 'Entry succesfully added!')
    def post(self):
        """
        CREATE an entry
        """
        data = request.json
        return add_entry(data=data)
