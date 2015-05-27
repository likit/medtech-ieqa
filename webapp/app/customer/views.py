from flask import render_template
from .forms import RegisterForm
from . import customer

@customer.route('/register')
def register():
    form = RegisterForm()
    return render_template('/customers/register.html', form=form)
