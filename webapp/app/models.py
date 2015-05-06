from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db

class Customer(UserMixin, db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Customer %r>' % self.name


from . import login_manager

@login_manager.user_loader
def load_user(customer_id):
    return Customer.query.get(int(customer_id))
