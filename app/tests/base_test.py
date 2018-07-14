#base_test.py
from flask_testing import TestCase

from manage import app
from app.main.model.entries import mock_db, MockDB



class BaseTestCase(TestCase): 
    """
    The Base Test Case 
    """ 
    def create_app(self): 
        """
        The method that creates an instance of the app
        """
        app.config.from_object('app.main.config.TestingConfig') 
        return app     
    
    def setUp(self):
        """
        The setUp for the Base Test Case
        : app
        : client
        : entry
        """
        self.app = app
        self.client = self.app.test_client
        self.app.testing = True
        self.entry = {
            'id' : 1,
            'title': 'My Day on the Moon',
            'content': 'So today was a very interesting day on the because I had 2 chicken drumsticks on the moon',
        }

        MockDB.entries.append(self.entry)

       
    def tearDown(self):
        pass