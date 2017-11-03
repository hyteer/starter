from flask import Blueprint

debug = Blueprint('debug', __name__, template_folder='templates')

from . import views
