# -*- coding: utf-8 -*-
"""
    YtEgg
    ~~~~~~
    An simple app by YT
"""
import os
from flask import Flask, g
from werkzeug.utils import find_modules, import_string
from .config import DefaultConfig
from .model import db, User
from . import model

APP_NAME = DefaultConfig.PROJECT


def create_app(config=None):
    print('init app...')
    app = Flask(APP_NAME)

    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'flaskr.db'),
        DEBUG=True,
        SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
        USERNAME='admin',
        PASSWORD='default'
    ))
    app.config.from_object(DefaultConfig)
    register_blueprints(app)
    configure_extensions(app)
    register_cli(app)
    register_teardowns(app)
    print("app is ready now...")

    return app


def configure_extensions(app):
    # flask-sqlalchemy
    db.init_app(app)
    #app.config["db"] = db
    #app.config['model'] = model

def register_blueprints(app):
    """Configure blueprints in views."""

    bps = ['user','todo']
    modules = {}
    for bp in bps:
        try:
            modules[bp] = (__import__(APP_NAME+'.'+bp,fromlist=["*"]))
        except ImportError:
            print("Error importing blueprint", bp)
    for bp in bps:
        #import pdb; pdb.set_trace()
        app.register_blueprint(getattr(modules[bp],bp),url_prefix='/'+bp)
    #### old fashion
    #from .user import user
    #from .todo import todo
    #app.register_blueprint(todo, url_prefix='/todo')
    #app.register_blueprint(user, url_prefix='/user')
    return None

def register_cli(app):
    @app.cli.command('initdb')
    def initdb_command():
        """Creates the database tables."""
        print('drop all...')
        db.drop_all()
        db.create_all()
        print('Initialized the database.')

def register_teardowns(app):
    @app.teardown_appcontext
    def close_db(error):
        """Closes the database again at the end of the request."""
        if hasattr(g, 'sqlite_db'):
            g.sqlite_db.close()
