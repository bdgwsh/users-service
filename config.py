import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'usersdb.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
PORT = 8000
