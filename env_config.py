"""
Simple config file
"""


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = b''  # TODO
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Dev(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
