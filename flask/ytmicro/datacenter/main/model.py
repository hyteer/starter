from flask_sqlalchemy import SQLAlchemy
from .extensions import db

#db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Unicode(128),nullable=False)
    username = db.Column(db.Unicode(128))
    password = db.Column(db.Unicode(128))

    def __repr__(self):
        return '<User %r>' % self.username


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Unicode(128),nullable=False)
    description = db.Column(db.String(128))
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Todo %r>' % self.title
