author = 'yt'
from flask_socketio import SocketIO, emit
from .manager import create_app, register_blueprints
app = create_app()
socketio = SocketIO(app)
register_blueprints(app)
