#test_config.py
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app

class TestDevelopmentConfig(TestCase):
    """
    Test Dev Config
    """
    def create_app(self):
        """
        Create an instance of the app
        """
        app.config.from_object('app.main.config.DevelopmentConfig')
        return app

    # 1 . Test Dev Config
    def test_app_config_is_dev(self):
        """
        Test Dev Config
        """
        self.assertFalse(app.config['SECRET_KEY'] is '4frocod3')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        
class TestTestingConfig(TestCase):
    """
    Test Test Config
    """
    def create_app(self):
        """
        Create an instance of the app
        """
        app.config.from_object('app.main.config.TestingConfig')
        return app

    # 2 . Test Test Config
    def test_app_config_is_test(self):
        self.assertFalse(app.config['SECRET_KEY'] is '4frocod3')
        self.assertTrue(app.config['DEBUG'])
        
class TestProductionConfig(TestCase):
    """
    Test Prod Config
    """
    def create_app(self):
        """
        Create an instance of the app
        """
        app.config.from_object('app.main.config.ProductionConfig')
        return app

    # 3 . Test Prod Config
    def test_app_config_is_prod(self):
        self.assertFalse(app.config['SECRET_KEY'] is '4frocod3')
        self.assertTrue(app.config['DEBUG'] is False)
        
if __name__ == '__main__':
    unittest.main()
