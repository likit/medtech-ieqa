# -*- encoding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import (StringField, SubmitField, FloatField,
                        TextField, SelectField, PasswordField)
from wtforms.validators import (Required, Email,
                                    Length, EqualTo, Optional)

class RegisterForm(Form):
    org = StringField('org', validators=[Required()])
    name = StringField('name', validators=[Required()])
    labs = SelectField('labs', choices=[('', u'โปรดกรอกชื่อหน่วยงาน')],
            validators=[Required()])
    addlab = StringField('addlab', validators=[Required()])
    lastname = StringField('lastname', validators=[Required()])
    email = StringField('email', validators=[Required(), Email()])
    password = PasswordField('password',
            validators=[EqualTo('password2'), Required()])
    password2 = PasswordField('password', validators=[Required()])
    submit = SubmitField('Submit')


class ResultForm(Form):
    program_id = StringField('Program ID', validators=[Required()])

    # these info should be pull from db in the future
    methods = {
        'albumin': ['BCG', 'BCP', 'Vitros'],
        'alp': ['PNP AMP buff; IFCC', 'PNP AMP Buff; AACC',
            'PNP DEA buff; DGKC',
            'Vitros', 'Reflotron',
            'Beckman'],
        'alt': ['Kinetic37C/Kinetic-without pyridoxal',
            'Kinetic-pyridoxal',
            'Dade Behring',
            'Vitros',
            'Reflotron',
            'Beckman'],
        'ast': ['Kinetic37C/Kinetic-without pyridoxal',
            'Kinetic-pyridoxal',
            'Dade Behring',
            'Vitros',
            'Reflotron',
            'Beckman'],
        'bun': ['Enzyme Kinetic', 'Enzyme', 'Vitros', 'Reflotron'],
        'bilirubin': ['Jendrassik-Grof', 'Malloy-Evelyn', 'Vitros', 'Reflotron',
            'DCA/DPD', 'Diazonium'],
        'calcium': ['CPC/Asenazo', 'Vitros', 'ISE'],
        'chloride': ['Direct ISE', 'Indirect ISE', 'Vitros ISE', 'Reflotron'],
        'cholesterol': ['Enzyme Colorimetric', 'Vitros', 'Reflotron',
            'Dade Behring', 'Beckman'],
        'ck': ['CK-NAC/IFCC', 'Colorimetric', 'Vitros', 'Reflotron'],
        'creatinine': ['Jaffe Kinetic', 'Jaffe EP', 'Vitros', 'Enzyme',
            'Reflotron'],
        'ggt': ['Enzyme Kinetic', 'Enzyme Colorimetric', 'Dade Behring',
            'Vitros', 'Reflotron'],
        'glucose': ['GOD', 'HK', 'Vitros', 'Reflotron', 'GDH'],
        'hdl_chol': ['Direct Determination',
            'Phospho. Precip./Polyanion', 'Vitros',
            'Imm. Inhibition', 'Others'],
        'ldh': ['IFCC', 'SSCC', 'DGKC', 'Vitros', 'Beckman'],
        'ldl_chol': ['Direct Determination', 'Others'],
        'P': ['Molybdenum EP', 'Molybdenum UV', 'Vitros'],
        'K': ['Direct ISE', 'Indirect ISE', 'Vitros', 'Reflotron'],
        'protein': ['Biuret-Blank', 'Biuret-Unblank', 'Vitros'],
        'Na': ['Direct ISE', 'Indirect ISE', 'Vitros', 'Reflotron'],
        'trig': ['Enzyme Color Total TG', 'Glycerol Blank', 'Vitros',
            'Reflotron', 'Dade Behring'],
        'uric': ['Enzyme EP Blank', 'Enzyme EP Unblank', 'Vitros', 'Reflotron',
            'Dade Behring'],
    }

    albumin = FloatField('Albumin', validators=[Optional()])
    albumin_ = SelectField('albumin_method',
           choices=[(m,m) for m in methods['albumin']]
           )
    alp = FloatField('ALP', validators=[Optional()])
    alp_ = SelectField('alp_method',
           choices=[(m,m) for m in methods['alp']]
           )
    alt = FloatField('ALT (SGPT)', validators=[Optional()])
    alt_ = SelectField('alt_method',
           choices=[(m,m) for m in methods['alt']]
           )
    ast = FloatField('AST (SGOT)', validators=[Optional()])
    ast_ = SelectField('ast_method',
           choices=[(m,m) for m in methods['ast']]
           )
    bun = FloatField('BUN', validators=[Optional()])
    bun_ = SelectField('bun_method',
            choices=[(m,m) for m in methods['bun']]
            )
    bilirubin = FloatField('Bilirubin, Total', validators=[Optional()])
    bilirubin_ = SelectField('bilirubin_method',
           choices=[(m,m) for m in methods['bilirubin']]
           )
    calcium = FloatField('Calcium, Total', validators=[Optional()])
    calcium_ = SelectField('calcium_method',
           choices=[(m,m) for m in methods['calcium']]
           )
    chloride = FloatField('Chloride', validators=[Optional()])
    chloride_ = SelectField('chloride_method',
           choices=[(m,m) for m in methods['chloride']]
           )
    cholesterol = FloatField('Cholesterol', validators=[Optional()])
    cholesterol_ = SelectField('cholesterol_method',
           choices=[(m,m) for m in methods['cholesterol']]
           )
    ck = FloatField('CK, Total', validators=[Optional()])
    ck_ = SelectField('ck_method',
           choices=[(m,m) for m in methods['ck']]
           )
    creatinine = FloatField('Creatinine', validators=[Optional()])
    creatinine_ = SelectField('creatinine_method',
           choices=[(m,m) for m in methods['creatinine']]
           )
    ggt = FloatField('GGT', validators=[Optional()])
    ggt_ = SelectField('ggt_method_method',
           choices=[(m,m) for m in methods['ggt']]
           )
    glucose = FloatField('Glucose', validators=[Optional()])
    glucose_ = SelectField('glucose_method',
           choices=[(m,m) for m in methods['glucose']]
           )
    hdl_chol = FloatField('HDL-Cholesterol', validators=[Optional()])
    hdl_chol_ = SelectField('hdl_chol_method',
           choices=[(m,m) for m in methods['hdl_chol']]
           )
    ldh = FloatField('LDH', validators=[Optional()])
    ldh_ = SelectField('ldh_method',
           choices=[(m,m) for m in methods['ldh']]
           )
    ldl_chol = FloatField('LDL-Cholesterol', validators=[Optional()])
    ldl_chol_ = SelectField('ldl_chol_method',
           choices=[(m,m) for m in methods['ldl_chol']]
           )
    P = FloatField('Phosphorus', validators=[Optional()])
    P_ = SelectField('P_method',
           choices=[(m,m) for m in methods['P']]
           )
    K = FloatField('Potassium', validators=[Optional()])
    K_ = SelectField('K_method',
           choices=[(m,m) for m in methods['K']]
           )
    protein = FloatField('Protein, Total', validators=[Optional()])
    protein_ = SelectField('protein_method',
           choices=[(m,m) for m in methods['protein']]
           )
    Na = FloatField('Sodium', validators=[Optional()])
    Na_ = SelectField('Na_method',
           choices=[(m,m) for m in methods['Na']]
           )
    trig = FloatField('Triglycerides', validators=[Optional()])
    trig_ = SelectField('trig_method',
           choices=[(m,m) for m in methods['trig']]
           )
    uric = FloatField('Uric acid', validators=[Optional()])
    uric_ = SelectField('uric_method',
            choices=[(m,m) for m in methods['uric']]
            )
    comment = TextField('Comment', validators=[Optional()])
    submit = SubmitField('Submit')
