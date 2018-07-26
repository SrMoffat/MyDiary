#base_test.py
import json

from flask_testing import TestCase

from manage import app
from app.main.model.users import User

class BaseTestCase(TestCase):
    """
    The Base Class for the Tests
    """
    signup_uri = "api/v2/auth/signup"
    login_uri = "api/v2/auth/login"
    @staticmethod
    def create_app():
        """
        Testing instance of the App
        """
        app.config.from_object("app.main.config.TestingConfig")
        return app

    def setUp(self):
        """
        Common variables for tests
        """
        self.app = app
        self.client = self.app.test_client(self)
        self.app.testing = True
        self.invalid_username = {
            "username":"4fr0c0d3",
            "email":"4fr0c0d3@mail.com",
            "password":"4fr0c0d3!"
        }
        self.user = {
            "username":"TestUser",
            "email":"4fr0c0d3@mail.com",
            "password":"4fr0c0d3!"
        }
        self.user_login = {
            "email":"4fr0c0d3@mail.com",
            "password":"4fr0c0d3!"
        }
        self.entry_payload = {
            "title":"My Day on the Moon",
            "content":"Rivers, shivers, dealers, triggers"
        }
        self.update_entry_payload = {
            "title":"My Updated Day in Space",
            "content":"Planters, herbalists, natural, utopia"
        }

    def user_signup_and_login(self):
        """
        POST :self.user: to api/v2/auth/signup
        then
        POST :self.login: to api/v2/auth/login
        """
        self.client.post(self.signup_uri,
                         data=json.dumps(self.user),
                         content_type="application/json")
        response = self.client.post(self.login_uri,
                                    data=json.dumps(self.user_login),
                                    content_type="application/json")
        return response

    def tearDown(self):
        pass