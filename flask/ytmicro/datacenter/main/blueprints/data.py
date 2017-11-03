from flask import Blueprint, jsonify, url_for, render_template
from flask import current_app as app
import json

bp = Blueprint('data', __name__)

@bp.route('/')
def index():
    return 'datacenter home.'

@bp.route('/test')
def test():
    return render_template('test.html')
