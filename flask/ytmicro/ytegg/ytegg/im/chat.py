from flask import jsonify, url_for, render_template, g, request
from flask import current_app as app
import json
from flask_socketio import emit, send, join_room, leave_room
from . import im
from . import config
from ..model import db, Todo
from ytegg import socketio

users = ['silly','yt','tony']

## routes

@im.route('/imroom')
def testroom():
    return render_template('im/imroom.html',room_id='001')
## imroom
@socketio.on('connect', namespace='/imroom')
def handle_connect():
    print("/imroom, new connect:")
    #import pdb; pdb.set_trace()
    emit('system', "/imroom connected.")

@socketio.on('disconnect', namespace='/imroom')
def handle_connect():
    print("/imroom, new connect:")
    #import pdb; pdb.set_trace()
    emit('system', "/imroom connected.")

@socketio.on('join', namespace='/imroom')
def on_join(data):
    print('Data:',data)
    username = data['username']
    room = data['room']
    join_room(room)
    if room == '11':
        import pdb; pdb.set_trace()
    print(username+' has joined '+'r:'+room+', sid:%s' % request.sid)
    emit('join',username + ' has entered the room.', room=room)
    #send(username + ' has entered the room.', room=room)

@socketio.on('debug', namespace='/imroom')
def handle_json(json):
    print('/imroom:debug: ' + str(json))
    action = json['action']
    args = json['args']
    resp = '...'
    if action == 'rooms':
        resp = 'rooms:%s' % socketio.server.rooms(request.sid)
    if action == 'pdb':
        import pdb; pdb.set_trace()
    emit('debug', 'debugInfo:%s' % resp)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)

@socketio.on('test', namespace='/imroom')
def handle_json(json):
    print('/imroom:test: ' + str(json))
    emit('test', '/imroom resp:%s' % json)

## imchat
@im.route('/chat')
def chat():
    return render_template('im/chat.html')

@socketio.on('testim', namespace='/chat')
def handle_json(msg):
    #import pdb; pdb.set_trace()

    print('/chat:testim: ' + str(msg))

    emit('testim', msg, broadcast=True)

## socketio


@socketio.on('test', namespace='/chat')
def handle_json(json):
    print('/chat:test: ' + str(json))
    emit('test', '/chat resp:%s' % json)

@socketio.on('system', namespace='/chat')
def handle_json(json):
    print('/chat:system: ' + str(json))
    emit('system', '/chat system:%s' % json)

@socketio.on('json', namespace='/chat')
def handle_my_custom_namespace_event(json):
    print('/chat:json: ' + str(json))
