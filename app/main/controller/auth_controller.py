#auth_controller.py
from flask import request
from flask_restplus import Resource

from ..utils.dto import UserDto
from ..service.auth_service import add_user

auth = UserDto.auth
user = UserDto.user

@auth.route("/signup")
class UserAuth(Resource):
    """
    USER AUTHENTICATION Resource
    """
    @auth.expect(user, validate=True)
    @auth.response(201, "Successfully registered!")
    def post(self):
        """
        CREATE a user
        """
        data = request.json
        return add_user(data)