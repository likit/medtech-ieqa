# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for
from flask.ext.login import current_user, logout_user
from .forms import RegisterForm
from . import customer
from .. import db
from bson import json_util
from werkzeug.security import generate_password_hash

@customer.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated():
        logout_user()

    form = RegisterForm()
    form.org.choices = [('', u'โปรดเลือก')] +\
            sorted([(x.get('name'), x.get('name'))
                for x in db.orgs.find()], key=lambda x: x[0])

    orgs = [x[0] for x in form.org.choices]

    if form.validate_on_submit():
        if form.org.data != '':
            new_org = None
        else:
            new_org = form.new_org.data

        new_customer = {
                'name': form.name.data,
                'lastname': form.lastname.data,
                'password': generate_password_hash(form.password.data),
                'org': form.org.data or None,
                'new_org': new_org,
                'email': form.email.data,
                }

        db.customers.insert(new_customer, safe=True)
        return redirect(url_for('auth.login'))

    return render_template('/customers/register.html',
            form=form,
            orgs = json_util.dumps(orgs))
