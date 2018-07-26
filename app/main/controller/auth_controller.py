#auth_controller.py
from flask import request
from flask_restplus import Resource

from ..utils.dto import UserDto
from ..service.auth_service import add_user, login_user

auth = UserDto.auth
signup_model = UserDto.signup_model
login_model = UserDto.login_model


@auth.route("/signup")
class SignUp(Resource):
    """
    USER SIGNUP Resource
    """
    @auth.doc("Add New User")
    @auth.doc(
        responses={
            201:"Successfully registered!",
            409:"Username exists!",
            400:"Invalid Input!"
        })
    @auth.expect(signup_model, validate=True)
    def post(self):
        """
        CREATE a user
        """
        data = request.json
        return add_user(data)

@auth.route("/login")
class Login(Resource):
    """
    USER LOGIN Resource
    """    
    @auth.doc("Login User")
    @auth.expect(login_model, validate=True)
    @auth.doc(
        responses={
            200:"Successfully logged in!",   
            401:"Invalid credentials!"
        })
    def post(self):
        """
        LOGIN a user
        """
        data = request.json
        return login_user(data)