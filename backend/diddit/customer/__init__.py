from flask import Blueprint

customer = Blueprint(
        'profile',
        __name__,
        template_folder='templates',
        static_folder='static'
)

#from . import views
