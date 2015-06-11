# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, flash
from flask.ext.login import current_user, logout_user
from .forms import RegisterForm, ResultForm
from . import customer
from .. import mongo
from bson import json_util
from werkzeug.security import generate_password_hash
from datetime import datetime
from ..models import get_result_id

@customer.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated():
        logout_user()

    form = RegisterForm()
    form.org.choices = [('', u'โปรดเลือก')] +\
            sorted([(x.get('name'), x.get('name'))
                for x in mongo.db.orgs.find()], key=lambda x: x[0])

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

        mongo.db.customers.insert(new_customer, safe=True)
        return redirect(url_for('auth.login'))

    return render_template('/customers/register.html',
            form=form,
            orgs = json_util.dumps(orgs))

@customer.route('/results_1', methods=['POST', 'GET'])
def results():
    form = ResultForm()
    if form.validate_on_submit():
        # TODO: need to look up program id from the db
        result_id = get_result_id(form.program_id.data)

        new_results = {
            'entered_at': datetime.now(),
            'entered_by': current_user.email,
            'program_id': form.program_id.data,
            'comment': form.comment.data,
            'subprogram': 1,
            'result_id': result_id,

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
            # Fields below are for future use.
            #'edited_at': datetime.now()
            'albumin_method' : form.albumin_.data,
            'alp_method' : form.alp_.data,
            'alt_method' : form.alt_.data,
            'ast_method' : form.ast_.data,
            'bun_method' : form.bun_.data,
            'bilirubin_method' : form.bilirubin_.data,
            'calcium_method' : form.calcium_.data,
            'chloride_method' : form.chloride_.data,
            'cholesterol_method' : form.cholesterol_.data,
            'ck_method' : form.ck_.data,
            'creatinine_method' : form.creatinine_.data,
            'ggt_method' : form.ggt_.data,
            'glucose_method' : form.glucose_.data,
            'hdl_chol_method' : form.hdl_chol_.data,
            'ldh_method' : form.ldh_.data,
            'ldl_chol_method' : form.ldl_chol_.data,
            'P_method' : form.P_.data,
            'K_method' : form.K_.data,
            'protein_method' : form.protein_.data,
            'Na_method' : form.Na_.data,
            'trig_method' : form.trig_.data,
            'uric_method' : form.uric_.data,
        }

        mongo.db.results.insert(new_results, safe=True)
        flash('Results number %s has been successfully saved to the database.'
                % str(result_id))
        return redirect(url_for('.results'))
    return render_template('/customers/results.html', form=form)
