import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    PORT = os.getenv('APP_PORT', '80')
    HOST = os.getenv('APP_HOST', '0.0.0.0')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
