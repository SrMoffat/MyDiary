#entry_controller.py

from flask import request
from flask_restplus import Resource

from ..utils.dto import EntryDto
from ..service.entry_service import add_entry

api = EntryDto.api
entry_model = EntryDto.entry_model


@api.route("/entries")
class Entries(Resource):
    """
    ENTRIES Resource
    """
    @api.doc("Add New User")
    @api.doc(
        responses={
            201:"Added entry!",
            409:"Entry exists!!",
            400:"Invalid Input!"
        },
        security="apiKey")
    @api.expect(entry_model, validate=True)
    def post(self, user_id):
        """
        CREATE an entry
        """
        data = request.json
        return add_entry(data, user_id)
