#test_auth.py
import unittest
import json 

from .base_test import BaseTestCase
from app.main.model.users import User

class TestAuth(BaseTestCase):
    """
    Test Class for User Authentication
    """
    
    # 1. POST api/v2/auth/signup
    def test_user_signup(self):
        """
        Test POST api/v2/auth/signup (valid user)
        """
        with self.client:
            response = self.user_signup_and_login()
            self.assertEqual(response.status_code, 200)
            result = json.loads(response.data)
            self.assertEqual(result["username"], "4fr0c0d3")
