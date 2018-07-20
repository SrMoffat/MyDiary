#test_auth.py
import json 

from .base_test import BaseTestCase
from app.main.model.users import User

class TestUser(BaseTestCase):
    """
    Test Class for Users
    """
    # def post_admin(self):
    #     return self.client().post('api/v1/auth/signup', 
    #                              data=json.dumps(self.admin_holder),
    #  
    #                             content_type='application/json')
    
    def post_user(self):
        return self.client().post('api/v1/auth/signup', 
                                 data=json.dumps(self.user_holder),
                                 content_type='application/json')    
    # def post_null_user(self):
    #     return self.client().post('api/v1/auth/signup', 
    #                              data=json.dumps(self.null_user_holder),
    #                              content_type='application/json')

    # def post_empty_string_user(self):
    #     return self.client().post('api/v1/auth/signup', 
    #                              data=json.dumps(self.empty_string_user_holder),
    #                              content_type='application/json')    
    # def post_int_user(self):
    #     return self.client().post('api/v1/auth/signup', 
    #                              data=json.dumps(self.int_user_holder),
    #                              content_type='application/json')
    # def post_null_password_user(self):
    #     return self.client().post('api/v1/auth/signup', 
    #                              data=json.dumps(self.null_password_user_holder),
    #                              content_type='application/json')

    
     # 1. POST api/v1/auth/signup
    def test_add_admin(self):
        """
        Test POST api/v1/auth/signup
        """
        with self.client(): 
            import pdb;pdb.set_trace()           
            response = self.post_user()  
            self.assertEqual(response.status_code, 201)      
            result = json.loads(response.data)        
            self.assertEqual(result["message"], "Successfully registered!")
            self.assertEqual(result["user"]["clearance"], 1)

    # # 1b. POST api/v1/entries
    # def test_cannot_add_existing_title(self):
    #     """
    #     Test POST api/v1/entries
    #     """
    #     with self.client():
    #         response = self.post_entry()            
    #         double_entry = response
    #         double_entry_result = json.loads(double_entry.data)
    #         self.assertEqual(double_entry_result["error"], "Entry already exists!")

    # # 1c. POST api/v1/entries  
    # def test_null_values_rejected(self):
    #     """
    #     Test POST api/v1/entries
    #     """
    #     with self.client():
    #         response = self.post_null_entry()
    #         self.assertEqual(response.status_code, 400)
    #         result = json.loads(response.data)
    #         self.assertEqual(result["error"], "All fields required!")

    # # 1d. POST api/v1/entries
    # def test_empty_string_rejected(self):
    #     """
    #     Test POST api/v1/entries
    #     """
    #     with self.client():
    #         response = self.post_empty_string_entry()
    #         self.assertEqual(response.status_code, 400)
    #         result = json.loads(response.data)
    #         self.assertEqual(result["error"], "All fields required!")
    
    # # 1e. POST api/v1/entries
    # def test_input_is_string(self):
    #     """
    #     Test POST api/v1/entries
    #     """
    #     with self.client():
    #         response = self.post_int_entry()
    #         self.assertEqual(response.status_code, 400)
    #         result = json.loads(response.data)
    #         self.assertEqual(result["message"], "Input payload validation failed")       


    # #2. GET api/v1/entries
    # def test_get_entries(self):
    #     """
    #     Test GET api/v1/entries
    #     """ 
    #     with self.client():
    #         self.post_entry()
    #         result = self.client().get('api/v1/entries', 
    #                                 content_type='application/json')
    #         self.assertEqual(result.status_code, 200)
    #         result_data = json.loads(result.data)
    #         self.assertEqual(result_data["entries"][0]["title"], "My Test Title on the Moon")

