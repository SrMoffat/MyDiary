#config.py
import os

class Config(object):
    SECRET_KET = os.getenv('SECRET_KEY')
    DEBUG = False
    TESTING = False
    RESTPLUS_VALIDATE = True

class DevelopmentConfig(Config):
    DEBUG = True
class TestingConfig(Config):
    DEBUG = True
    TESTING = True
class ProductionConfig(Config):
    DEBUG = False
app_configs = {
    'dev' : DevelopmentConfig,
    'test': TestingConfig,
    'prod' : ProductionConfig
    }
