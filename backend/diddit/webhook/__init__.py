from flask import Blueprint

webhook = Blueprint('webhook',
        __name__,
        template_folder='templates',
        static_folder='static')

from . import views
