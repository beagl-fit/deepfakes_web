from flask_sqlalchemy import SQLAlchemy
from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.Boolean, default=False, nullable=False)
    age = db.Column(db.Integer, default=None, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    # answers = db.relationship('Answer', backref='user', lazy='dynamic')

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question = db.Column(db.Integer, nullable=False)
    answer = db.Column(db.Integer, nullable=False)