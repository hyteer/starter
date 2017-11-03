from flask import Blueprint, jsonify, url_for, current_app,render_template,request
import json

bp = Blueprint('debug', __name__, url_prefix='/debug', template_folder='templates')

@bp.route('/')
def index():
    addr = request.remote_addr
    resp = "debug...</br>addr:%s" % addr
    
    return resp


@bp.route('/info')
def info():
    return render_template("debug/info.html")
