#test_auth.py
import unittest
import json 

from .base_test import BaseTestCase
from app.main.model.users import User

class TestAuth(BaseTestCase):
    """
    Test Class for User Authentication
    """
    signup_uri = "api/v2/auth/signup"
    login_uri = "api/v2/auth/login"

    def register_user(self):
        """
        POST :self.user: to api/v2/auth/signup
        """

        return self.client.post(self.signup_uri,
                         data=json.dumps(self.user),
                         content_type="application/json")
    def login_user(self):
        """
        POST :self.login: to api/v2/auth/login
        """
        return self.client.post(self.login_uri,
                                    data=json.dumps(self.user_login),
                                    content_type="application/json")
    
    # 1. POST api/v2/auth/signup
    def test_user_signup(self):
        """
        Test POST api/v2/auth/signup (valid user)
        """

        with self.client:
            response = self.register_user()
            self.assertEqual(response.status_code, 201)
            result = json.loads(response.data)
            self.assertEqual(result["username"], "TestUser3")
