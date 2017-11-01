from flask import jsonify, g, url_for, current_app, render_template, request,session,flash,\
redirect
from flask import current_app as app
import json
from ytegg.user import user
from . import config
from ..model import db, User


######################### Db
#with current_app.app_context():
#    pass

@user.route('/')
def index():
    return 'user home.'

@user.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username).first_or_404()
        if not user:
            error = 'Invalid username'
        elif request.form['password'] != user.password:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('user.users'))
    return render_template('user/login.html', error=error)

@user.route('/users')
def users():
    users = db.session.query(User)
    return render_template("user/users.html", users=users)

@user.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User()
            form.populate_obj(new_user)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/users')
    return render_template('user/create_user.html', form=form)

@user.route('/test')
def test():
    #import pdb; pdb.set_trace()
    URL = config.TEST_URL
    print("TestUrl:",URL)
    #return "TestUrl:%s" % URL
    return render_template('user/test.html')
