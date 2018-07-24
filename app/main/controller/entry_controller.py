#entry_controller.py
from flask import request 
from flask_restplus import Resource

from ..utils.dto import EntryDto
from ..service.entry_service import add_entry, get_all_entries, get_one_entry, modify_entry, remove_entry

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

    @api.marshal_with(entry, envelope='entries')
    @api.response(200, 'Successfully fetched entries!')
    def get(self):
        """
        FETCH entries
        """
        return get_all_entries()

@api.route('/entries/<entry_id>')
@api.param('entry_id' , 'The identifier for the entry')
@api.response(404, 'Entry not found!')
class Entry(Resource):
    """
    The Single Entry Resource for the API
    """
    @api.marshal_with(entry, envelope='entry')
    @api.response(200, 'Successfully fetched an entry!')
    def get(self, entry_id):
        """
        FETCH an entry
        """
        return get_one_entry(entry_id)

    def put(self, entry_id):
        """
        MODIFY an entry
        """
        data = request.json
        return modify_entry(entry_id, data)

    def delete(self, entry_id):
        """
        REMOVE an entry
        """
        return remove_entry(entry_id)
           
