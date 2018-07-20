#base_test.py
import uuid
from flask_testing import TestCase

from manage import app
from app.main.model.entries import MockDB,Entry

class BaseTestCase(TestCase): 
    """
    The Base Test Case 
    """ 
    @classmethod
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
        self.entry = Entry(title='My Test Title on the Moon',content='So today was a very interesting day on the because I had 2 chicken drumsticks on the moon')    
        self.null_entry = Entry(title='',content='')
        self.empty_string_entry = Entry(title='Title on the Moon',content='                 ')
        self.int_entry = Entry(title=1,content=12345)
        self.entry_holder = self.entry.display_entry_holder()
        self.null_entry_holder = self.null_entry.display_entry_holder()
        self.empty_string_entry_holder = self.null_entry.display_entry_holder()
        self.int_entry_holder = self.int_entry.display_entry_holder()
       
    def tearDown(self):
        pass
        