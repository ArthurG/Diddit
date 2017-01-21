from flask import Flask
import json
from flask_sqlalchemy import SQLAlchemy
from diddit import db
import requests

class User(db.Model):
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    location = db.Column(db.String(500), nullable = False)
    lat = db.Column(db.Float(500), nullable = True)
    lng = db.Column(db.Float(500), nullable = True)
    username = db.Column(db.String(500), nullable = False)
    password = db.Column(db.String(500), nullable = False)
    def __init__(self, location, username, password):
        self.location = location
        data={'address':location}
        endpoint="https://maps.googleapis.com/maps/api/geocode/json"
        resp = requests.get(endpoint, params=data)
        latlng = json.loads(resp.text)['results'][0]['geometry']['location']
        self.lat = latlng['lat']
        self.lng = latlng['lng']
        self.username = username
        self.password = password
db.create_all()
