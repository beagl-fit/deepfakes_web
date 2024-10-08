from DFWeb_app import db


class Users(db.Model):
    """
    :var sex: False: Male; True: Female
    :var age: 0-3: [<18, 18-25, 26-55, >55]
    :var encountered:(deepfakes) False: not encountered, True: encountered
    """
    id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.Boolean, default=False, nullable=False)
    age = db.Column(db.Integer, default=0, nullable=False)
    encountered = db.Column(db.Boolean, default=False, nullable=False)
    answers = db.relationship('Answers', backref='user')


class Answers(db.Model):
    """
    :var user_id: [FK] id of answering user
    :var question: question number
    :var answer_1: pre-test answer
    :var answer_2: post-test answer
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    question = db.Column(db.Integer, default=0, nullable=False)
    answer_1 = db.Column(db.Boolean, default=False, nullable=False)
    answer_2 = db.Column(db.Boolean, default=False, nullable=False)


class Publications(db.Model):
    """
    :var name: publication name [100]
    :var description: short summary of publication [250]
    :var link: url of the publication [-]
    :var deleted: boolean; default false
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    link = db.Column(db.String(), nullable=False)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
