from flask import Blueprint

customer = Blueprint(
        'customer',
        __name__,
        template_folder='templates',
        static_folder='static'
)

from . import views
