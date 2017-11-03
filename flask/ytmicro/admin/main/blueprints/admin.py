from flask import Blueprint, jsonify, url_for, render_template
from flask import current_app as app
import json

bp = Blueprint('admin', __name__)

@bp.route('/')
def index():
    return 'admin home.'

@bp.route('/test')
def test():
    return render_template('test.html')
