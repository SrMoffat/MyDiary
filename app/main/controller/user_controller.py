#user_controller.py
from flask import request 
from flask_restplus import Resource

from ..utils.dto import UserDto
from ..service.user_service import save_new_user, get_one_user, get_users,remove_user,modify_user

auth = UserDto.auth
user = UserDto.user

@auth.route('/signup')
class Users(Resource):
    """
    The User Resource for the API
    """
    @auth.expect(user, validate=True)
    @auth.response(201, 'Succesfully registered!')
    def post(self):
        """
        CREATE a user
        """
        data = request.json
        return save_new_user(data=data)

    @auth.marshal_with(user, envelope="users")
    @auth.response(200, 'Successfully fetched!')
    def get(self):
        """
        FETCH users
        """
        return get_users()

@auth.route('/signup/<user_id>')
@auth.param('<user_id>' , 'The User identifier')
@auth.response(404, 'User does not exist!')
class SingleUser(Resource):
    """
    The User Resource for the API
    """
    @auth.marshal_with(user, envelope="user")
    def get(self, user_id):
        """
        FETCH one user
        """
        user = get_one_user(user_id)
        if not user:
            auth.abort(404)
        else:
            return user

    def put(self, user_id):
        """
        MODIFY an user's clearance
        """        
        return modify_user(user_id)

    def delete(self, user_id):
        """
        REMOVE a user
        """
        return remove_user(user_id)
    