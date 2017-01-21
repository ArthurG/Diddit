from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .webhook import webhook
from .customer import customer
from database import db

diddit = Flask (__name__)
diddit.config['SQLALCHEMY_DATABASE_URI']="sqlite:///diddit.db3"
diddit.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
diddit.register_blueprint(webhook)
diddit.register_blueprint(customer)

db.init_app(diddit)

#db = SQLAlchemy(diddit)
