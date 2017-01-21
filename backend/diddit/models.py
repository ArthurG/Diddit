from flask import Flask
import json
from flask_sqlalchemy import SQLAlchemy
from diddit import db
import requests

class User(db.Model):
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    location = db.Column(db.String(500), nullable = False)
    store_name = db.Column(db.String(500), nullable = False)
    lat = db.Column(db.Float(500), nullable = True)
    lng = db.Column(db.Float(500), nullable = True)
    username = db.Column(db.String(500), nullable = False)
    password = db.Column(db.String(500), nullable = False)

    def __init__(self, location, storename, username, password):
        self.location = location
        self.store_name = storename
        data={'address':location}
        endpoint="https://maps.googleapis.com/maps/api/geocode/json"
        resp = requests.get(endpoint, params=data)
        latlng = json.loads(resp.text)['results'][0]['geometry']['location']
        self.lat = latlng['lat']
        self.lng = latlng['lng']
        self.username = username
        self.password = password

class Survey(db.Model):
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    survey_name = db.Column(db.String(500), nullable = False)
    user_name = db.Column(db.Integer, db.ForeignKey('user.id'))
    user=db.relationship('User', backref=db.backref('surveys', lazy='dynamic'))

class Surveyquestion(db.Model):
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    questionName = db.Column(db.String(500), nullable = False)
    questionType = db.Column(db.String(500), nullable = False)
    survey_name = db.Column(db.Integer, db.ForeignKey('survey.id'))
    survey=db.relationship('Survey', backref=db.backref('questions', lazy='dynamic'))

class SurveyQuestionAnswer(db.Model):
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    answerString = db.Column(db.String(500), nullable = False)
    surveyquestion_name = db.Column(db.Integer, db.ForeignKey('surveyquestion.id'))
    surveyquestion=db.relationship('Surveyquestion', backref=db.backref('answers', lazy='dynamic'))

db.create_all()
