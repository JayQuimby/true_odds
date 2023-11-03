from . import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class form(FlaskForm):
    name = StringField(label='name')
    resp = StringField(label='response')
    submit = SubmitField(label='submit')
