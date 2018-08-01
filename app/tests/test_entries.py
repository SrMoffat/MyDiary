# test_entries.py
import json
import unittest

from .base_test import BaseTestCase
from .helper_methods import register_user, login_user

class TestEntries(BaseTestCase):
    """
    Test class for entry operations
    """
    def test_add_entry(self):
        with self.client:
            response = register_user(self)
            self.assertEqual(response.status_code, 201)
            response = login_user(self)
            self.assertEqual(response.status_code, 200)
            result = json.loads(response.data)            
            self.assertIn("You are now logged in!", result["message"])
            self.assertIn("success!", result["status"])
            self.assertIn("token", result)
            response = self.client.post("api/v2/entries",
                                        headers={
                                            "token":result["token"],
                                            "content-type":"application/json"
                                        },
                                        data=self.post_entry)
            result = json.loads(response.data)
            self.assertEqual(response.status_code, 201)
            self.assertIn("Entry added!", result[u"message"])
            self.assertIn("success!", result[u"status"])
    def test_get_all_entries(self):
        with self.client:
            response = register_user(self)
            self.assertEqual(response.status_code, 201)
            response = login_user(self)
            self.assertEqual(response.status_code, 200)
            result = json.loads(response.data)            
            self.assertIn("You are now logged in!", result["message"])
            self.assertIn("success!", result["status"])
            self.assertIn("token", result)
            token = result["token"]
            response = self.client.post("api/v2/entries",
                                        headers={
                                            "token":token,
                                            "content-type":"application/json"
                                        },
                                        data=self.post_entry)
            result = json.loads(response.data)
            self.assertEqual(response.status_code, 201)
            self.assertIn("Entry added!", result[u"message"])
            self.assertIn("success!", result[u"status"])
            response = self.client.get("api/v2/entries",
                                        headers={
                                            "token":token,
                                            "content-type":"application/json"
                                        })
            self.assertEqual(response.status_code, 200)
            result = json.loads(response.data)                      
            self.assertIn("Test entry post", result[u"entries"][0][u"title"])
    def test_get_entry_by_id(self):
        with self.client:
            response = register_user(self)
            self.assertEqual(response.status_code, 201)
            response = login_user(self)
            self.assertEqual(response.status_code, 200)
            result = json.loads(response.data)
            self.assertIn("token", result)
            token = result["token"]
            response = self.client.post("api/v2/entries",
                                        headers={
                                            "token":token,
                                            "content-type":"application/json"
                                        },
                                        data=self.post_entry)
            self.assertEqual(response.status_code, 201)            
            response = self.client.get("api/v2/entries/1",
                                        headers={
                                            "token":token,
                                            "content-type":"application/json"
                                        })
            self.assertEqual(response.status_code, 200)
    def test_entry_modification(self):
        with self.client:
            response = register_user(self)
            self.assertEqual(response.status_code, 201)
            response = login_user(self)
            self.assertEqual(response.status_code, 200)
            result = json.loads(response.data)
            self.assertIn("token", result)
            token = result["token"]
            response = self.client.post("api/v2/entries",
                                        headers={
                                            "token":token,
                                            "content-type":"application/json"
                                        },
                                        data=self.post_entry)
            self.assertEqual(response.status_code, 201)
            response = self.client.put("api/v2/entries/1",
                                        headers={
                                            "token":token,
                                            "content-type":"application/json"
                                        },
                                        data=self.update_entry)
            self.assertEqual(response.status_code, 200)
    def test_delete_entry(self):
        with self.client:
            response = register_user(self)
            self.assertEqual(response.status_code, 201)
            response = login_user(self)
            self.assertEqual(response.status_code, 200)
            result = json.loads(response.data)
            token = result["token"]
            response = self.client.post("api/v2/entries",
                                        headers={
                                            "token":token,
                                            "content-type":"application/json"
                                        },
                                        data=self.post_entry)
            self.assertEqual(response.status_code, 201)
            response = self.client.delete("api/v2/entries/1",
                                        headers={
                                            "token":token,
                                            "content-type":"application/json"
                                        })
            self.assertEqual(response.status_code, 200)
            