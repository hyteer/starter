from flask import Blueprint

im = Blueprint('im', __name__, template_folder='templates')

from . import views,chat,wsock
