from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from . import login_manager

class Customer():
    def __init__(self, email):
        self.email = email

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email

    def __repr__(self):
        return '<Customer: email %r>' % self.email


@login_manager.user_loader
def load_user(email):
    customer = db.customers.find_one({'email': email})
    if not customer:
        return None
    else:
        return Customer(customer['email'])
