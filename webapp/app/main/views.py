from . import main
from flask import render_template, flash
from .forms import Result
from flask.ext.login import login_required

@main.route('/')
@login_required
def index():
    flash("You're logged in successfully.")
    return render_template('index.html')

@main.route('/result/', methods=['GET', 'POST'])
def result():
    form = Result()
    if form.validate_on_submit():
        flash('Success!')
    return render_template('result.html', form=form)
