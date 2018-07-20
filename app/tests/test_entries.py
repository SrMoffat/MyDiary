# test_entries.py
import json
import datetime 

from .base_test import BaseTestCase
from app.main.model.entries import Entry

class TestEntries(BaseTestCase):
    """
    Test Class for Entries
    """
    def post_entry(self):
        return self.client().post('api/v1/entries', 
                                 data=json.dumps(self.entry_holder),
                                 content_type='application/json')
    
    def post_null_entry(self):
        return self.client().post('api/v1/entries', 
                                 data=json.dumps(self.null_entry_holder),
                                 content_type='application/json')

    def post_empty_string_entry(self):
        return self.client().post('api/v1/entries', 
                                 data=json.dumps(self.empty_string_entry_holder),
                                 content_type='application/json')
    
    def post_int_entry(self):
        return self.client().post('api/v1/entries', 
                                 data=json.dumps(self.int_entry_holder),
                                 content_type='application/json')
    
    # 1. POST api/v1/entries
    def test_add_entry(self):
        """
        Test POST api/v1/entries
        """
        with self.client():
            response = self.post_entry()  
            self.assertEqual(response.status_code,201)      
            result = json.loads(response.data)        
            self.assertEqual(result["message"],"Entry Added!")
            self.assertEqual(result["entry"]["title"],"My Test Title on the Moon")

    # 1b. POST api/v1/entries
    def test_cannot_add_existing_title(self):
        """
        Test POST api/v1/entries
        """
        with self.client():
            response = self.post_entry()            
            double_entry = response
            double_entry_result = json.loads(double_entry.data)
            self.assertEqual(double_entry_result["error"],"Entry already exists!")

    # 1c. POST api/v1/entries  
    def test_null_values_rejected(self):
        """
        Test POST api/v1/entries
        """
        with self.client():
            response = self.post_null_entry()
            self.assertEqual(response.status_code,400)
            result = json.loads(response.data)
            self.assertEqual(result["error"],"All fields required!")

    # 1d. POST api/v1/entries
    def test_empty_string_rejected(self):
        """
        Test POST api/v1/entries
        """
        with self.client():
            response = self.post_empty_string_entry()
            self.assertEqual(response.status_code,400)
            result = json.loads(response.data)
            self.assertEqual(result["error"],"All fields required!")
    
    # 1e. POST api/v1/entries
    def test_input_is_string(self):
        """
        Test POST api/v1/entries
        """
        with self.client():
            response = self.post_int_entry()
            self.assertEqual(response.status_code,400)
            result = json.loads(response.data)
            self.assertEqual(result["message"],"Input payload validation failed")       


    #2. GET api/v1/entries
    def test_get_entries(self):
        """
        Test GET api/v1/entries
        """ 
        with self.client():
            self.post_entry()
            result = self.client().get('api/v1/entries', 
                                    content_type='application/json')
            self.assertEqual(result.status_code,200)
            result_data = json.loads(result.data)
            self.assertEqual(result_data["entries"][0]["title"],"My Test Title on the Moon")

    #3. GET api/v1/entries/<entry_id>
    def test_get_one_entry(self):
        """
        Test GET api/v1/entries/<entry_id>
        """ 
        with self.client():            
            self.post_entry()            
            result = self.client().get('api/v1/entries', 
                                    content_type='application/json')
            self.assertEqual(result.status_code,200)
            result_data = json.loads(result.data)
            self.assertEqual(result_data["entries"][0]["title"],"My Test Title on the Moon")




   
        
