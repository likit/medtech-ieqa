from flask.ext.wtf import Form
from wtforms import (StringField, SubmitField,
                        IntegerField, SelectField, PasswordField)
from wtforms.validators import Required, Email, Length, EqualTo

class RegisterForm(Form):
    org = SelectField('org', validators=[Required()])
    new_org = StringField('new_org')
    name = StringField('name', validators=[Required()])
    lastname = StringField('lastname', validators=[Required()])
    email = StringField('email', validators=[Required(), Email()])
    password = PasswordField('password',
            validators=[EqualTo('password2'), Required()])
    password2 = PasswordField('password', validators=[Required()])
    submit = SubmitField('Submit')
