# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, flash, jsonify, request
from flask.ext.login import current_user, logout_user
from .forms import RegisterForm, ResultForm
from . import customer
from .. import mongo
from bson import json_util
from werkzeug.security import generate_password_hash
from datetime import datetime
from ..models import get_result_id
import numpy as np

@customer.route('/getlabs')
def get_labname():
    org = request.args.get('org', 'unknown')
    labs = [o['labname']
            if o else '' for o in mongo.db.orgs.find({'name': org})]
    return jsonify(labs=labs)

@customer.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated():
        logout_user()

    form = RegisterForm()
    orgs = {'source': sorted([x.get('name')
                    for x in mongo.db.orgs.find()], key=lambda x: x[0])}

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
            orgs=orgs)

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

@customer.route('/report/<progid>')
def report(progid):
    # test_methods = set()
    # for r in mongo.db.results.find():
    #     if r[test_method]:
    #         test_methods.add(r[test_method])

    # test_values = {}
    # for m in test_methods:
    #     tests = []
    #     for r in mongo.db.results.find({test_method: m}):
    #         if r[test_name]:
    #             tests.append(r[test_name])
    #     test_values[m] = tests

    # all_methods = []

    def calculate(values, sd_range):
        mean = np.mean(values)
        std = np.std(values)
        N = len(values)
        CV = std/mean * 100.0
        upper = mean + sd_range * std
        lower = mean - sd_range * std
        return {'mean': mean,
                'std': std,
                'N': N,
                'CV': CV,
                'upper': upper,
                'lower': lower,
                'test_name': test_name}


    # def filter_values(values, sd_range):
    #     """Returns values within std range"""
    #     mean = np.mean(values)
    #     std = np.std(values)
    #     upper = mean + (sd_range * std)
    #     lower = mean - (sd_range * std)
    #     filtered_values = []
    #     for val in values:
    #         if upper >= val >= lower:
    #             filtered_values.append(val)

    #     return filtered_values


    # for m in test_methods:
    #     calculate(test_values[m], m, 1.5)
    #     all_methods += test_values[m]

    # principle = "All"
    values = []
    test_name = 'glucose'
    for r in mongo.db.results.find():
        val = r[test_name]
        #TODO: rewrite this line to honor 0
        if val:
            values.append(val)


    stats = calculate(values, 1.5)
    cust_res = mongo.db.results.find_one({'program_id': progid})
    cust_gluc = cust_res['glucose']
    print stats

    # for m in test_methods:
    #     filtered_values = filter_values(test_values[m], 3)
    #     calculate(filtered_values, 'New ' + m, 1.5)

    # filtered_values = filter_values(all_methods, 3)
    # calculate(filtered_values, 'New all', 1.5)

    return render_template('/customers/report.html', stats=stats,
            cust_gluc=cust_gluc)
