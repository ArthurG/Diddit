from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db
from . import db

class User(db.Model):
    uid = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable = False)
    cron_news = db.Column(db.boolean(192), nullable = False)
