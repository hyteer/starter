from flask import jsonify, url_for, render_template
from flask import current_app as app
import json
from . import main
from . import config
from ..model import db, Todo

@main.route('/')
def index():
    return 'home.'

@main.route('/todo/')
def todo():
    return 'Parent覆盖todo11.'

@main.route('/test')
def test():
    #import pdb; pdb.set_trace()
    URL = config.TEST_URL
    print("TestUrl:",URL)
    #return "TestUrl:%s" % URL
    return render_template('test.html')
