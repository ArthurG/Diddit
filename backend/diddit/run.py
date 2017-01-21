import json
import sys

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

def setup_database(app):
    with app.app_context():
        db = SQLAlchemy()
        db.create_al()
    

def log(message):  # simple wrapper for logging to stdout on heroku
    print(str(message))
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
    setup_database(app)
