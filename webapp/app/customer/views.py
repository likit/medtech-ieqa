# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for
from flask.ext.login import current_user, logout_user
from .forms import RegisterForm, ResultForm
from . import customer
from .. import db
from bson import json_util
from werkzeug.security import generate_password_hash
from datetime import datetime

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

@customer.route('/results', methods=['POST', 'GET'])
def results():
    form = ResultForm()
    if form.validate_on_submit():
        new_results = {
            'albumin' : form.albumin.data,
            'alp' : form.alp.data,
            'alt' : form.alt.data,
            'ast' : form.ast.data,
            'bun' : form.bun.data,
            'bilirubin' : form.bilirubin.data,
            'calcium' : form.calcium.data,
            'chloride' : form.chloride.data,
            'cholesterol' : form.cholesterol.data,
            'ck' : form.ck.data,
            'creatinine' : form.creatinine.data,
            'ggt' : form.ggt.data,
            'glucose' : form.glucose.data,
            'hdl_chol' : form.hdl_chol.data,
            'ldh' : form.ldh.data,
            'ldl_chol' : form.ldl_chol.data,
            'P' : form.P.data,
            'K' : form.K.data,
            'protein' : form.protein.data,
            'Na' : form.Na.data,
            'trig' : form.trig.data,
            'uric' : form.uric.data,
            'entered_at': datetime.now(),

            # Fields below are for future use.
            #'entered_by': user.name
            #'edited_at': datetime.now()
            #'program_id': program_id
            #'result_id': get_result_id()
        }

        db.results.insert(new_results, safe=True)
        return redirect(url_for('auth.login'))
    return render_template('/customers/results.html', form=form)
