from flask.ext.wtf import Form
from wtforms import (StringField, PasswordField,
        BooleanField, SubmitField, FloatField)
from wtforms.validators import Required, Email, Optional
from flask_admin.contrib.pymongo import ModelView
from .. import mongo

class AdminLoginForm(Form):
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class AdminResultForm(Form):
    albumin = FloatField('Albumin', validators=[Optional()])
    uric = FloatField('Uric', validators=[Optional()])
    glucose = FloatField('Glucose', validators=[Optional()])
    submit = SubmitField('Save')
