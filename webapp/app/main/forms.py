from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Required

class Result(Form):
    albumin = IntegerField('Albumin', validators=[Required()])
    alp = IntegerField('ALP', validators=[Required()])
    submit = SubmitField('Submit')
