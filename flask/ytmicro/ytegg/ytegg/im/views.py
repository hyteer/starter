from flask import jsonify, url_for, render_template, g
from flask import current_app as app
import json
from flask_socketio import emit
from . import im
from . import config
from ..model import db, Todo
from ytegg import socketio



@im.route('/')
def index():
    return 'todo home.'

@im.route('/tasks')
def tasks():
    #Todo = app.config['model'].Todo
    #db = app.config['db']
    tasks = db.session.query(Todo)
    #import pdb; pdb.set_trace()
    return render_template("im/tasks.html", tasks=tasks)

@im.route('/client')
def client():
    return render_template('im/client.html')

@im.route('/test')
def test():
    URL = config.TEST_URL
    print("TestUrl:",URL)
    #return "TestUrl:%s" % URL
    return render_template('im/test.html')

@socketio.on('connect')
def handle_connect():
    print("/, new connect:")
    emit('system', "/ connected.")

@socketio.on('system')
def handle_system(message):
    print("/:system:",message)
    emit('system', 'system msg...')

@socketio.on('message')
def handle_message(message):
    print('/:message: ' + message)
    emit('message', 'resp:%s' % message)

@socketio.on('test')
def handle_test(message):
    print("/:test:",message)
    emit('test', 'msg:%s' % message)



#### Use namespace
@socketio.on('connect', namespace='/test')
def handle_connect():
    print("/test, new connect:")
    emit('system', "/test connected.")

@socketio.on('test', namespace='/test')
def handle_json(json):
    print('/test:test: ' + str(json))
    emit('test', '/test resp:%s' % json)

@socketio.on('system', namespace='/test')
def handle_json(json):
    print('/test:system: ' + str(json))
    emit('system', '/test system:%s' % json)

@socketio.on('json', namespace='/test')
def handle_my_custom_namespace_event(json):
    print('/test:json: ' + str(json))
