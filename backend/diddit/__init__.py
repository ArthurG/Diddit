from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .webhook import webhook
from .customer import customer

diddit = Flask (__name__)
diddit.register_blueprint(webhook)
diddit.register_blueprint(customer)

db = SQLAlchemy(diddit)
