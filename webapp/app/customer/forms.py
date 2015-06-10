from flask.ext.wtf import Form
from wtforms import (StringField, SubmitField, FloatField,
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


class ResultForm(Form):
    albumin = FloatField('Albumin')
    alp = FloatField('ALP')
    alt = FloatField('ALT (SGPT)')
    ast = FloatField('AST (SGOT)')
    bun = FloatField('BUN')
    bilirubin = FloatField('Bilirubin, Total')
    calcium = FloatField('Calcium, Total')
    chloride = FloatField('Chloride')
    cholesterol = FloatField('Cholesterol')
    ck = FloatField('CK, Total')
    creatinine = FloatField('Creatinine')
    ggt = FloatField('GGT')
    glucose = FloatField('Glucose')
    hdl_chol = FloatField('HDL-Cholesterol')
    ldh = FloatField('LDH')
    ldl_chol = FloatField('LDL-Cholesterol')
    P = FloatField('Phosphorus')
    K = FloatField('Potassium')
    protein = FloatField('Protein, Total')
    Na = FloatField('Sodium')
    trig = FloatField('Triglycerides')
    uric = FloatField('Uric acid')

    # these info should be pull from db in the future
    methods = {
        'albumin': ['BCG', 'BCP', 'Vitros'],
        'alp': ['PNP AMP buff; IFCC', 'PNP AMP Buff; AACC',
            'PNP DEA buff; DGKC',
            'Vitros', 'Beckman', 'Reflotron'],
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
        'creatinine': ['Jaffe Kinetric', 'Jaffe EP', 'Vitros', 'Enzyme',
            'Reflotron'],
        'ggt': ['Enzyme Kinetic', 'Enzyme Colorimetric', 'Dade Behring',
            'Vitros', 'Reflotron'],
        'glucose': ['GOD', 'HK', 'Vitros', 'Reflotron', 'GDH'],
        'hdl_chol': ['Direct Determination',
            'Phospho. Precip./Polyanion', 'Vitros',
            'Imm. Inhibition', 'Others'],
        'ldh': ['IFCC', 'SSCC', 'DGKC', 'Vitros', 'Beckman'],
        'ldl_chol': ['Direct Determination', 'AU480', 'Others'],
        'P': ['Molybdenum EP', 'Molybdenum UV', 'Vitros'],
        'K': ['Direct ISE', 'Indirect ISE', 'Vitros', 'Reflotron'],
        'protein': ['Biuret-Blank', 'Biuret-Unblank', 'Vitros'],
        'Na': ['Direct ISE', 'Indirect ISE', 'Vitros', 'Reflotron'],
        'trig': ['Enzyme Color Total TG', 'Glycerol Blank', 'Vitros',
            'Reflotron', 'Dade Behring'],
        'uric': ['Enzyme EP Blank', 'Enzyme EP Unblank', 'Vitros', 'Reflotron',
            'Dade Behring'],
    }
    albumin_ = SelectField('albumin_method',
           choices=[(m,m) for m in methods['albumin']]
           )
    alp_ = SelectField('alp_method',
           choices=[(m,m) for m in methods['alp']]
           )
    alt_ = SelectField('alt_method',
           choices=[(m,m) for m in methods['alt']]
           )
    ast_ = SelectField('ast_method',
           choices=[(m,m) for m in methods['ast']]
           )
    bun_ = SelectField('bun_method',
            choices=[(m,m) for m in methods['bun']]
            )
    bilirubin_ = SelectField('bilirubin_method',
           choices=[(m,m) for m in methods['bilirubin']]
           )
    calcium_ = SelectField('calcium_method',
           choices=[(m,m) for m in methods['calcium']]
           )
    chloride_ = SelectField('chloride_method',
           choices=[(m,m) for m in methods['chloride']]
           )
    cholesterol_ = SelectField('cholesterol_method',
           choices=[(m,m) for m in methods['cholesterol']]
           )
    ck_ = SelectField('ck_method',
           choices=[(m,m) for m in methods['ck']]
           )
    creatinine_ = SelectField('creatinine_method',
           choices=[(m,m) for m in methods['creatinine']]
           )
    ggt_ = SelectField('ggt_method_method',
           choices=[(m,m) for m in methods['ggt']]
           )
    glucose_ = SelectField('glucose_method',
           choices=[(m,m) for m in methods['glucose']]
           )
    hdl_chol_ = SelectField('hdl_chol_method',
           choices=[(m,m) for m in methods['hdl_chol']]
           )
    ldh_ = SelectField('ldh_method',
           choices=[(m,m) for m in methods['ldh']]
           )
    ldl_chol_ = SelectField('ldl_chol_method',
           choices=[(m,m) for m in methods['ldl_chol']]
           )
    P_ = SelectField('P_method',
           choices=[(m,m) for m in methods['P']]
           )
    K_ = SelectField('K_method',
           choices=[(m,m) for m in methods['K']]
           )
    protein_ = SelectField('protein_method',
           choices=[(m,m) for m in methods['protein']]
           )
    Na_ = SelectField('Na_method',
           choices=[(m,m) for m in methods['Na']]
           )
    trig_ = SelectField('trig_method',
           choices=[(m,m) for m in methods['trig']]
           )
    uric_ = SelectField('uric_method',
            choices=[(m,m) for m in methods['uric']]
            )
    submit = SubmitField('Submit')
