import os, click, sqlite3
from flask import Flask, g, redirect, url_for
from .config import DefaultConfig
from .model import db, User
from .todo import todo
from .user import user
from . import model

__all__ = ['create_app']

def create_app(config=None, app_name=None):
    """Create a Flask app."""
    if app_name is None:
        app_name = DefaultConfig.PROJECT
    app = Flask(app_name)
    app.register_blueprint(todo, url_prefix='/todo')
    app.register_blueprint(user, url_prefix='/user')
    app.config.from_object(DefaultConfig)
    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'test-egg.db'),
        SECRET_KEY='development key',
        USERNAME='admin',
        PASSWORD='admin'
    ))

    db.init_app(app)
    app.config["yteggdb"] = db
    app.config['model'] = model

    return app

app = create_app()


@app.route('/')
def index():
    return "home..."

@app.route('/login', methods=['GET', 'POST'])
def login():
    return redirect('user/login',next=url_for('index'))

@app.route('/debug')
def debug():
    import pdb; pdb.set_trace()
    return "debug..."

@app.route('/admin')
def admin():
    return '<a href="/admin/">Click me to get to Admin!</a>'

@app.cli.command('initdb')
def initdb():
    db.drop_all()
    db.create_all()

'''
if __name__ == '__main__':
    db.init_app(app)
    #db.create_all(app=app)
    app.run(debug=True,threaded=True)
'''
