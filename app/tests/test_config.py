#test_config.py

import os 
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app 
from app.main.config import basedir

class TestDevelopmentConfig(TestCase): 
    def create_app(self): 
        app.config.from_object('app.main.config.DevelopmentConfig') 
        return app

    def test_app_config_is_dev(self): 
        self.assertFalse(app.config['SECRET_KEY'] is '4frocod3')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)

class TestTestingConfig(TestCase): 
    def create_app(self): 
        app.config.from_object('app.main.config.TestingConfig') 
        return app

    def test_app_config_is_test(self): 
        self.assertFalse(app.config['SECRET_KEY'] is '4frocod3')
        self.assertTrue(app.config['DEBUG'])
        
class TestProductionConfig(TestCase): 
    def create_app(self): 
        app.config.from_object('app.main.config.ProductionConfig') 
        return app

    def test_app_config_is_prod(self): 
        self.assertFalse(app.config['SECRET_KEY'] is '4frocod3')
        self.assertTrue(app.config['DEBUG'] is False)
        
if __name__ == '__main__': 
    unittest.main()

