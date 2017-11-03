# -*- coding: utf-8 -*-
"""
    YtEgg
    ~~~~~~
    An simple app by YT
"""
import os
from flask import Flask, g
from .config import DefaultConfig
from werkzeug.utils import find_modules, import_string
from .model import db, User
from . import model
from .extensions import db

APP_NAME = DefaultConfig.PROJECT


def create_app(config=None):
    app = Flask(APP_NAME)
    app.config.from_object(DefaultConfig)
    #register_blueprints(app)
    configure_extensions(app)
    register_cli(app)
    register_teardowns(app)
    register_blueprints(app)
    return app


def configure_extensions(app):
    # flask-sqlalchemy
    db.init_app(app)
    #app.config["db"] = db
    #app.config['model'] = model

def register_blueprints(app):
    """Configure blueprints in views."""
    for name in find_modules('main.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)

    #import pdb; pdb.set_trace()
    return None

    ## Old fashion
    #from .blueprints import main
    #app.register_blueprint(main, url_prefix='/main')
    #app.register_blueprint(todo, url_prefix='/todo')
    #return None

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
