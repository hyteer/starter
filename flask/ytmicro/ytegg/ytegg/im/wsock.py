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

@im.route('/wstest')
def wstest():
    return render_template('im/wsclient.html')
