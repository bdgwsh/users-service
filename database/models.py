from .db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __repr__(self):
        return '<User %r>, id %r' % (self.login, self.id)
