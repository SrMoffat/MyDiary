#entry_controller.py

from flask import request
from flask_restplus import Resource

from ..utils.dto import EntryDto
from ..utils.decorators import token_required
from ..service.entry_service import add_entry, get_all_entries, get_one_entry, modify_entry, remove_entry

api = EntryDto.api
entry_model = EntryDto.entry_model


@api.route("/entries")
class Entries(Resource):
    """
    ENTRIES Resource
    """
    @api.doc("Add New Entry")
    @api.doc(
        responses={
            201:"Added entry!",
            409:"Entry exists!!",
            400:"Invalid Input!"
        },
        security="apiKey")
    @api.expect(entry_model, validate=True)
    @token_required
    def post(self, user_id):
        """
        ADD an entry
        """
        data = request.json
        return add_entry(data, self)

    @api.doc("Fetch all entries")
    @api.doc(
        responses={
            201:"Successfully fetched entries!",
            400:"Invalid Input!",
            404:"No entries found!",
        },
        security="apiKey")
    @api.marshal_with(entry_model, envelope="entries")
    @token_required
    def get(self, user_id):
        """
        FETCH all entries
        """
        return get_all_entries(self)

@api.route("/entries/<int:entry_id>")
class SingleEntry(Resource):
    """
    Single ENTRY Resource
    """
    @api.doc("Get an Entry")
    @api.doc(
        responses={
            200:"Fetch Successful!",
            400:"Bad Request!",
            404:"Entry not found!"
        },
        security="apiKey")
    @api.marshal_with(entry_model, envelope="entry")
    @token_required
    def get(self, user_id, entry_id):
        """
        FETCH an entry
        """
        try:
            return get_one_entry(entry_id, self)
        except:
            api.abort(404, "error: Entry with id: {} not found".format(entry_id))

    @api.doc("Modify an Entry")
    @api.doc(
        responses={
            200:"Fetch Successful!",
            400:"Bad Request!",
            404:"Entry not found!"
        },
        security="apiKey"
    )
    @token_required
    def put(self, user_id, entry_id):
        """
        MODIFY an entry
        """
        data = request.json
        return modify_entry(self, entry_id, data)

    @api.doc("Remove an Entry")
    @api.doc(
        responses={
            200:"Successfully deleted!",
            400:"Bad Request!",
            404:"Entry not found!"
        },
        security="apiKey")
    @token_required
    def delete(self, user_id, entry_id):
        """
        REMOVE an Entry
        """
        return remove_entry(user_id,entry_id)
