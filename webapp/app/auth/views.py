# -*- coding: UTF-8 -*-

from werkzeug.security import check_password_hash
from flask.ext.login import current_user
from flask import render_template, request, url_for, flash, redirect
from flask.ext.login import login_user, login_required, logout_user
from ..models import Customer
from .forms import LoginForm
from . import auth
from .. import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated():
        flash("You've been logged in.")
        redirect(url_for('main.index'))

    if form.validate_on_submit():
        customer = db.customers.find_one({'email': form.email.data})
        if customer is not None and check_password_hash(customer['password'],
                form.password.data):
            # login_user(customer, form.remember_me.data)
            login_user(Customer(customer['email']))
            return redirect(request.args.get('next')
                    or url_for('main.index'))
        flash('Invalid email or password')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
