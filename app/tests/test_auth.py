#test_auth.py
import unittest
import json 

from .base_test import BaseTestCase
from .helper_methods import register_user, login_user

class TestAuth(BaseTestCase):
    """
    Test Class for User Authentication
    """
    def test_user_signup(self):
        with self.client:
            response = register_user(self)
            result = json.loads(response.data)
            self.assertEqual(response.status_code, 201)
            self.assertIn("User registered!", result[u"message"])
            self.assertIn("success!", result[u"status"])
    def test_double_registration(self):
        with self.client:
            response = register_user(self)
            self.assertEqual(response.status_code, 201)
        with self.client:
            response = register_user(self)
            result = json.loads(response.data)
            self.assertEqual(response.status_code, 409)
            self.assertIn("Username exists!", result[u"message"])
            self.assertIn("failed!", result[u"status"])
    def test_invalid_username(self):
        with self.client:
            response = self.client.post('/api/v2/auth/signup',
                                        data=json.dumps(dict(
                                        username='4frocod3',
                                        email='mymail@mail.com',
                                        password='mypassword')),
                                        content_type='application/json'
                                        )
            result = json.loads(response.data)
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid characters in username!", result[u"error"])
            self.assertIn("failed!", result[u"status"])
    def test_invalid_email(self):
        with self.client:
            response = self.client.post('/api/v2/auth/signup',
                                        data=json.dumps(dict(
                                        username='CharsOnly',
                                        email='mymail@mail',
                                        password='mypassword')),
                                        content_type='application/json')
            result = json.loads(response.data)
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid email!", result[u"error"])
            self.assertIn("failed!", result[u"status"])
    def test_weak_password(self):
        with self.client:
            response = self.client.post('/api/v2/auth/signup',
                                        data=json.dumps(dict(
                                        username='Chhars',
                                        email='mymail@mail.com',
                                        password='myp')),
                                        content_type='application/json')
            result = json.loads(response.data)
            self.assertEqual(response.status_code, 400)
            self.assertIn("Password too weak!", result[u"error"])
            self.assertIn("failed!", result[u"status"])
    def test_user_login(self):
        with self.client:
            response = register_user(self)
            self.assertEqual(response.status_code, 201)
            response = login_user(self)
            result = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn("You are now logged in!" , result[u"message"])   
    def test_invalid_login_creds(self):
        with self.client:
            response = register_user(self)
            self.assertEqual(response.status_code, 201)
            response = self.client.post('/api/v2/auth/login',
                                        data=json.dumps(dict(
                                        username='TestUser',
                                        password='TestUserpas')),
                                        content_type='application/json')
            result = json.loads(response.data)
            self.assertEqual(response.status_code, 401)
            self.assertIn("failed!",result[u"status"])
            self.assertIn("Incorrect password!",result[u"message"])
    def test_login_unregistered_user(self):
        with self.client:
            response = login_user(self)
            result = json.loads(response.data)
            self.assertEqual(response.status_code, 401)
            self.assertIn("failed!",result[u"status"])
            self.assertIn("Invalid credentials!",result[u"error"])

   