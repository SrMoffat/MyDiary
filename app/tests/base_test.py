#base_test.py
import json

from flask_testing import TestCase

from manage import app
from app.main.model.db import DatabaseConnection
from app.main.model.users import User
from app.main.model.entries import Entry

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
        self.db = DatabaseConnection()
        self.cursor = self.db.cursor
        self.dict_cursor = self.db.dict_cursor
        self.db.create_tables()
        self.user = User(id=1,
                         username="Kalashnikov",
                         email="4k47ashkash@mail.com",
                         password="4k47ashkash")
        self.test_entry = Entry(id=1,
                                owner="1",
                                title="First Test Title",
                                content="This is the test content for the entry")
        self.post_entry = json.dumps({
            "title":"Test entry post",
            "content":"This is the test entry post content"
        })
        self.update_entry = json.dumps({
            "title":"Update test entry post",
            "content":"This is the update for the test entry post content"
        })
    
    def tearDown(self):
        self.db.drop_all()