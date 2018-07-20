#base_test.py
import uuid
from flask_testing import TestCase

from manage import app
from app.main.model.entries import MockDB, Entry
from app.main.model.users import User



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

        self.admin = User(username='4fr0c0d3',email='4fr@c0d3.com',password='4fr0c0d3p455',clearance=1)
        self.admin_holder = self.admin.display_user_holder()        
        self.user = User(username='us3r',email='us3r@c0d3.com',password='us3rp455')
        self.user_holder = self.user.display_user_holder()       
        self.null_user = User(username='',email='',password='us3rp455')
        self.null_user_holder = self.null_user.display_user_holder()
        self.empty_string_user = User(username='            ',email='us3r@c0d3.com',password='us3rp455')
        self.empty_string_user_holder = self.empty_string_user.display_user_holder()
        self.null_password_user = User(username='us3r',email='us3r@c0d3.com',password='')
        self.null_password_user_holder = self.null_password_user.display_user_holder()
        self.int_user = User(username=1,email='us3r@c0d3.com',password='us3rp455')
        self.int_user_holder = self.int_user.display_user_holder()

        self.entry = Entry(title='My Test Title on the Moon', content='So today was a very interesting day on the because I had 2 chicken drumsticks on the moon')    
        self.entry_holder = self.entry.display_entry_holder()
        self.int_entry = Entry(title=1, content=12345)
        self.int_entry_holder = self.int_entry.display_entry_holder()
        self.null_entry = Entry(title='', content='')
        self.null_entry_holder = self.null_entry.display_entry_holder()
        self.empty_string_entry = Entry(title='Title on the Moon', content='                 ')  
        self.empty_string_entry_holder = self.null_entry.display_entry_holder()
       
       
    def tearDown(self):
        pass
        