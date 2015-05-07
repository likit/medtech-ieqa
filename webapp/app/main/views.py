from . import main
from flask import render_template
from ..models import Test
from .forms import Result

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/test/<test_id>', methods=['GET', 'POST'])
def test(test_id):

    test = Test.query.filter_by(id=test_id).first()

    return render_template('test.html', test=test)

@main.route('/result/', methods=['GET', 'POST'])
def result():
    result_form = Result()
    return render_template('result.html', form=result_form)
