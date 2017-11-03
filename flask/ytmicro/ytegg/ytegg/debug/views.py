from flask import jsonify, url_for, current_app,render_template,request
import json
from . import debug
from . import config

@debug.route('/')
def index():
    addr = request.remote_addr
    resp = "debug...</br>addr:%s" % addr
    return resp

@debug.route('/info')
def info():
    return render_template("debug/info.html")
