from flask_login import UserMixin
from datetime import datetime

from database_config import db

user_time = db.Table('user_time',
                     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('date_id', db.Integer, db.ForeignKey('date.id')))

class User(UserMixin, db.Model):
    __table_name__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_lvl = db.Column(db.Integer)
    username = db.Column(db.String(30), unique=True)
    name = db.Column(db.String(30), unique=False)
    surname = db.Column(db.String(30), unique=False)
    midname = db.Column(db.String(30), unique=False)
    ticket = db.Column(db.String(50), unique=False)
    enddate = db.Column(db.String(50), unique=False)
    password = db.Column(db.String(80))
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    timelines = db.relationship('Date', secondary=user_time, backref='user')



class Date(UserMixin, db.Model):
    __table_name__ = 'date'
    id = db.Column(db.Integer, primary_key=True)
    people_count = db.Column(db.Integer)
    day = db.Column(db.String(15))
    date = db.Column(db.String(50))
    time = db.Column(db.String(80))
    users_id = db.relationship('User', secondary=user_time, backref='date')

