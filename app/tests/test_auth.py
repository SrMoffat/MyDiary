#test_auth.py
import jwt
import unittest
import json 

from .base_test import BaseTestCase
from app.main.model.users import User

class TestAuth(BaseTestCase):
    """
    Test Class for User Authentication
    """

    def register_user(self):
        """
        CREATE USER with POST api/v2/auth/signup
        """
        return self.client.post("api/v2/auth/signup", 
                                data=json.dumps(self.user),
                                content_type="application/json")
    def login_user(self):
        """
        LOGIN USER with POST api/v2/auth/login
        """
        return self.client.post("api/v2/auth/login",
                                data=json.dumps(self.login_user),
                                content_type="application/json")

    # 1. POST api/v2/auth/signup
    def test_user_signup(self):
        """
        Test POST api/v2/auth/signup (valid)
        """
        with self.client:
            response = self.register_user()
            self.assertEqual(response.status_code, 201)
            result = json.loads(response.data)
            self.assertEqual(result["username"], "4fr0c0d3")

    # 2. POST api/v2/auth/login
    def test_user_login(self):
        """
        Test POST api/v2/auth/login (valid)
        """
        with self.client:
            response = self.login_user()
            self.assertEqual(response.status_code, 200)
            result = json.loads(response.data)
            self.assertEqual(result["message"], "Successfully logged in!")