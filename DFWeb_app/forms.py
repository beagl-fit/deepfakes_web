# TODO: probably delete this
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, HiddenField, IntegerField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError, Length


class SessionForm(FlaskForm):
    sex = HiddenField('Sex', validators=[DataRequired()])
    # age = BooleanField('Age', validators=[DataRequired()])
    # encountered = BooleanField('Encountered', validators=[DataRequired()])

    # submit = SubmitField('Submit')
