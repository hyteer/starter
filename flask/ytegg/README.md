# Instructions

## Setup & Shell Usage
pip install --editable .
set FLASK_APP=flaskr
set FLASK_DEBUG=1
flask init_db
flask run -p 5001 --reload --with-threads

## DB operation
#### add
User = app.config['model'].User
db = app.config['yteggdb']
u1 = User(email='u1@qq.com')
u1.username = 'user1'
u1.password = '111'
db.session.add(u1)
db.session.commit()

Todo = app.config['model'].Todo
t1 = Todo(title='test1.',description='a test task.')
db.session.add(t1)
db.session.commit()
#### query
uq = User.query.filter_by(username='user1').first()
or
uq = User.query.filter_by(username='user1').first_or_404()
uq.email

## Blueprint structure
user = Blueprint('user', __name__, template_folder='templates',static_folder='static')

static:
user/static/user/test.txt
http://localhost:5000/user/static/user/test.txt

templates:
user/templates/user/test.html
render_template('user/test.html')

## Todo
* socketio/websocket
* notebook
* friends
* channe
* post
* profile
