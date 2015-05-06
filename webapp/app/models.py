from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db
from . import login_manager

class Customer(UserMixin, db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)

    password_hash = db.Column(db.String(128))

    org_id = db.Column(db.Integer, db.ForeignKey('orgs.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Customer:email %r>' % self.email


class Organization(db.Model):
    __tablename__ = 'orgs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    province = db.Column(db.String(128))

    customers = db.relationship('Customer', backref='org', lazy='dynamic')
    tests = db.relationship('Test', backref='org', lazy='dynamic')

    def __repr__(self):
        return '<Organization %r>' % self.name

class Test(db.Model):
    __tablename__ = 'tests'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(64))
    date = db.Column(db.DateTime)
    status = db.Column(db.Boolean)

    org_id = db.Column(db.Integer, db.ForeignKey('orgs.id'))


@login_manager.user_loader
def load_user(customer_id):
    return Customer.query.get(int(customer_id))
