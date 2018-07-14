# test_entries.py
import unittest
import json
import datetime 

from base_test import BaseTestCase
from app.main.model.entries import Entry

class TestEntries(BaseTestCase):

    # 1. POST api/v1/entries
    def test_add_entry(self):
        response = self.client().post('api/v1/entries', 
                                 data=json.dumps(self.entry),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

    # 2. GET api/v1/entries
    def test_get_entries(self):
        response = self.client().get('api/v1/entries', 
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # 3. GET api/v1/entries/<int:entry_id>
    def test_get_one_entry(self, id=1):
        response = self.client().get('api/v1/entries/1',
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)


    # 4. PUT api/v1/entries/<int:entry_id>
    def test_modify_entry(self, id=1):
        response = self.client().post('api/v1/entries', 
                                 data=json.dumps(self.entry),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        
        new_data = {            
            'title': 'My Modified Day on the Moon',
            'content': 'So today was a very modified day on the because I had 2 chicken drumsticks on the moon'            
        }
        response = self.client().put('api/v1/entries/1', 
                                 data=json.dumps(new_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
