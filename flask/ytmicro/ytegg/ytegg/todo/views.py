from flask import jsonify, url_for, render_template
from flask import current_app as app
import json
from . import todo
from . import config
from ..model import db, Todo

@todo.route('/')
def index():
    return 'todo home.'

@todo.route('/tasks')
def tasks():
    #Todo = app.config['model'].Todo
    #db = app.config['db']
    tasks = db.session.query(Todo)
    #import pdb; pdb.set_trace()
    return render_template("todo/tasks.html", tasks=tasks)

@todo.route('/test')
def test():
    #import pdb; pdb.set_trace()
    URL = config.TEST_URL
    print("TestUrl:",URL)
    #return "TestUrl:%s" % URL
    return render_template('todo/test.html')
