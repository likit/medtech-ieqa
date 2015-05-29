from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email, Length

class LoginForm(Form):
    email = StringField('Email', validators=[Required(),
                                                Email(), Length(1,64)])
    password = PasswordField('Password', validators=[Required()])
    # remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
