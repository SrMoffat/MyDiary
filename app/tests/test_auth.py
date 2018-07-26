#test_auth.py
import unittest
import json 

from .base_test import BaseTestCase
from app.main.model.users import User

class TestAuth(BaseTestCase):
    """
    Test Class for User Authentication
    """
    def register_user(self):
        return self.client.post("api/v2/auth/signup",
                                 data=json.dumps(self.user),
                                 content_type="application/json")
    def login_user(self):
        return self.client.post("api/v2/auth/login",
                                 data=json.dumps(self.user_login),
                                 content_type="application/json")
    #    
    def test_user_signup(self):
        """
        Test POST api/v2/auth/signup (valid user)
        """
        with self.client:
            self.assertEqual(self.register_user().status_code, 201)
            result = json.loads(self.register_user().data)         
            self.assertEqual(result['username'], 'MyTestUserI')
    #
    def test_invalid_username(self):
        """
        Test POST api/v2/auth/signup (invalid username)
        """
        response = self.client.post("api/v2/auth/signup",
                                 data=json.dumps({
                                    "username":"MyTestUserI",
                                    "email":"4fr0c0d3@mail.com",
                                    "password":"4fr0c0d3!"
                                                }),
                                 content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["error"], "Invalid characters in username!")
    #
    def test_invalid_email(self):
        """
        Test POST api/v2/auth/signup (invalid email)
        """
        response = self.client.post("api/v2/auth/signup",
                                 data=json.dumps({
                                    "username":"MyTestUserI",
                                    "email":"4fr0c0d3@mail",
                                    "password":"4fr0c0d3!"
                                                }),
                                 content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["error"], "Invalid email!")
    #
    def test_weak_password(self):
        """
        Test POST api/v2/auth/signup (weak_password)
        """
        response = self.client.post("api/v2/auth/signup",
                                 data=json.dumps({
                                    "username":"MyTestUserI",
                                    "email":"4fr0c0d3@mail.com",
                                    "password":"c0d3!"
                                                }),
                                 content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["error"], "Password too weak!")
    #
    def test_user_login(self):
        """
        Test POST api/v2/auth/login (valid user)
        """
        with self.client:
            self.assertEqual(self.login_user().status_code, 200)
            result = json.loads(self.login_user().data)            
            self.assertEqual(result['username'], 'MyTestUserI')

    def test_invalid_login(self):
        """
        Test POST api/v2/auth/login (invalid user credentials)
        """
        self.register_user()
        response = self.client.post("api/v2/auth/login",
                                 data=json.dumps({
                                    "username":"IamNotHere",
                                    "password":"c0d3!"
                                                }),
                                 content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["error"], "Invalid credentials!")
   