from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .webhook import webhook
from .profile import profile

diddit = Flask (__name__)
diddit.register_blueprint(webhook)
diddit.register_blueprint(profile)

db = SQLAlchemy(diddit)
