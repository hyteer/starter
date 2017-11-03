from flask import Blueprint, jsonify, url_for, render_template, request
from flask import current_app as app
import json, copy
from main.extensions import db
from main.model import User

bp = Blueprint('todo', __name__)
RESP = {'code':200,'data':None}

@bp.route('/', methods=['GET','POST'])
def user():
    resp = copy.copy(RESP)
    if request.method == 'GET':
        args = request.args
        if not args:
            return 'user home.'
        else:
            name = request.args.get('name')
            email = request.args.get('email')
            if name:
                user = User.query.filter_by(username=name).first()
            elif email:
                user = User.query.filter_by(email=email).first()
            else:
                user = None
            if user:
                resp.update(data=user.serialize)
            else:
                resp.update(code=4001)
            #import pdb; pdb.set_trace()
            print("RESP:%s" % RESP)
            return jsonify(resp)
    if request.method == 'POST':
        data = request.get_json()
        #import pdb; pdb.set_trace()
        print(data)
        try:
            #import pdb; pdb.set_trace()
            user = User(username=data['username'])
            user.email = data['email']
            user.password = data['password']
            db.session.add(user)
            db.session.commit()
        except:
            resp.update(code=5001)
            return jsonify(resp)
        resp.update(msg='success')
        return jsonify(resp)
    if request.method == 'DELETE':
        data = request.get_json()
        print(data)
        return 'NotImplemented'


@bp.route('/users')
def users():
    users = User.query.limit(10).all()
    resp.update(data=[i.serialize for i in users])
    #import pdb; pdb.set_trace()
    return jsonify(resp)

@bp.route('/test')
def test():
    return render_template('test.html')
