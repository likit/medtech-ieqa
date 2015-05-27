from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Required, Email, Length

class RegisterForm(Form):
    name = StringField('Name', validators=[Required()])
    lastname = StringField('Lastname', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    submit = SubmitField('Submit')
