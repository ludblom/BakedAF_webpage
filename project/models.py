from flask_login import UserMixin
from . import db
import sqlalchemy as sa


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))
    uname = db.Column(db.String(100))

    def __repr__(self):
        return '<uname: {}>'.format(self.uname)


class SplitData(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(128))
    event_value = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = sa.orm.relationship(User)

    def __repr__(self):
        return '<event_name: {}, event_value: {}>'.format(event_name, event_value)
