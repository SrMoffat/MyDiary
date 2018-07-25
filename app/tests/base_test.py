#base_test.py
import uuid

from flask_testing import TestCase

from manage import app
from app.main.model.users import User

class BaseTestCase(TestCase):
    """
    The Base Class for the Tests
    """
    def create_app(self):
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
        self.client = self.app.test_client()
        self.app.testing = True
        self.user = User(
            id=1,
            username="4fr0c0d3",
            email="4fr0c0d3@mail.com",
            password="4fr0c0d3!"
        )
        self.user_login = {
            "username":"4fr0c0d3",
            "password" :"4fr0c0d3!"
        }
        
