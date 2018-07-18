# test_entries.py
import unittest
import json
import datetime 

from base_test import BaseTestCase
from app.main.model.entries import Entry

class TestEntries(BaseTestCase):
    """
    Test Class for Entries
    """

    # 1. POST api/v1/entries
    def test_add_entry(self):
        """
        Test POST api/v1/entries
        """
        response = self.client().post('api/v1/entries', 
                                 data=json.dumps(self.entry_holder),
                                 content_type='application/json')
        
        result = json.loads(response.data)        
        self.assertEqual(result["message"], "Entry Added!")
        self.assertEqual(result["entry"]["title"], "My Test Title on the Moon")

    # 1b. POST api/v1/entries
    def test_cannot_add_existing_title(self):
        """
        Test POST api/v1/entries
        """
        response = self.client().post('api/v1/entries', 
                                 data=json.dumps(self.entry_holder),
                                 content_type='application/json')        
        double_entry = self.client().post('api/v1/entries', 
                                 data=json.dumps(self.entry_holder),
                                 content_type='application/json')
        double_entry_result = json.loads(double_entry.data)
        self.assertEqual(double_entry_result["error"], "Entry already exists!")

    # 1c. POST api/v1/entries  
    def test_null_values_rejected(self):
        """
        Test POST api/v1/entries
        """
        response = self.client().post('api/v1/entries',
                                       data=json.dumps(self.null_entry_holder),
                                       content_type='application/json')       
        self.assertEqual(response.status_code, 400)

    # 1d. POST api/v1/entries
    def test_empty_string_rejected(self):
        """
        Test POST api/v1/entries
        """
        response = self.client().post('api/v1/entries',
                                       data=json.dumps(self.empty_string_entry_holder),
                                       content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)        
        self.assertEqual(result["error"], "All fields required!")
        
    
    # 1e. POST api/v1/entries
    def test_input_is_string(self):
        """
        Test POST api/v1/entries
        """
        response = self.client().post('api/v1/entries',
                                       data=json.dumps(self.int_entry_holder),
                                       content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Input payload validation failed")
        


    # 2. GET api/v1/entries
    # def test_get_entries(self):
    #     """
    #     Test GET api/v1/entries
    #     """
    #     response = self.client().get('api/v1/entries', 
    #                             content_type='application/json')
    #     self.assertEqual(response.status_code, 200)




    # 3. PUT api/v1/entries/<int:entry_id>
    # def test_modify_entry(self, id=1):
    #     """
    #     Test PUT api/v1/entries/<int:entry_id>
    #     """
    #     response = self.client().post('api/v1/entries', 
    #                              data=json.dumps(self.entry),
    #                              content_type='application/json')
    #     self.assertEqual(response.status_code, 500)
        
    #     new_data = {            
    #         'title': 'My Modified Day on the Moon',
    #         'content': 'So today was a very modified day on the because I had 2 chicken drumsticks on the moon',
    #         'date created' : str(datetime.datetime.utcnow)           
    #     }
        # response = self.client().put('api/v1/entries/1', 
        #                          data=json.dumps(new_data),
        #                          content_type='application/json')
        # self.assertEqual(response.status_code, 400)
        
