#base_test.py
import json
from datetime import datetime
from flask_testing import TestCase

from manage import app
from app.main.model.entries import mock_db, MockDB


class BaseTestCase(TestCase):
    
    def setUp(self):
        self.app = app.config.from_object('app.main.config.TestingConfig')
        self.app.testing = True
        self.app = self.app.test_client()
        self.entry = {
            'id' : 1,
            'title': 'My Day on the Moon',
            'content': 'So today was a very interesting day on the because I had 2 chicken drumsticks on the moon',
            'posted on' : datetime.utcnow()
        }

        MockDB.entries.append(self.entry)

       
    def tearDown(self):
        pass