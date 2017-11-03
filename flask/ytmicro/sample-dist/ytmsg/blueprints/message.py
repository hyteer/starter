from flask import Blueprint, jsonify, url_for, render_template
from flask import current_app as app
import json

bp = Blueprint('message', __name__, url_prefix='/message')

@bp.route('/')
def index():
    return 'message home.'

@bp.route('/test')
def test():
    return render_template('test.html')
