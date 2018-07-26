#base_test.py
import json

from flask_testing import TestCase

from manage import app
from app.main.model.users import User

class BaseTestCase(TestCase):
    """
    The Base Class for the Tests
    """
    
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
            "username":"TestUser2",
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

    
    def tearDown(self):
        pass