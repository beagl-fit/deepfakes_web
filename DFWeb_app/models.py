from DFWeb_app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.Boolean, default=False, nullable=False)
    age = db.Column(db.Integer, default=0, nullable=False)
    encountered = db.Column(db.Boolean, default=False, nullable=False)
    # answers = db.relationship('Answer', backref='user', lazy='dynamic')


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question = db.Column(db.Integer, default=0, nullable=False)
    answer_1 = db.Column(db.Boolean, default=False, nullable=False)
    answer_2 = db.Column(db.Boolean, default=False, nullable=False)
