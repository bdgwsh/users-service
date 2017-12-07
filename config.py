import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'usersdb.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    PORT = 8000
