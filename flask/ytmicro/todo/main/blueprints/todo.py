from flask import Blueprint, jsonify, url_for, render_template
from flask import current_app as app
import json

bp = Blueprint('todo', __name__)

@bp.route('/')
def index():
    return 'todo home.'

@bp.route('/test')
def test():
    return render_template('test.html')
