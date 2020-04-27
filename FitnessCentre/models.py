from flask_login import UserMixin
from database_config import db

class User(db.Model, UserMixin):
    __table_name__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

class Date(UserMixin, db.Model):
    __table_name__ = 'time'
    id = db.Column(db.Integer, primary_key=True)
    people = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(15), unique=True)
    date = db.Column(db.String(50), unique=True)
    time = db.Column(db.String(80))