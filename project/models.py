from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))
    uname = db.Column(db.String(100))
    splitdata = db.relationship('SplitData', backref='author', lazy='dynamic')


class SplitData(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(100), db.ForeignKey('user.uname'))
