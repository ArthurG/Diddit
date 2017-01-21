from flask import Flask
import json
from flask_sqlalchemy import SQLAlchemy
from database import db
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
        print(self.location, self.store_name, self.lat, self.lng, self.username, self.password)

class Survey(db.Model):
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    survey_name = db.Column(db.String(500), nullable = False)
    user_name = db.Column(db.Integer, db.ForeignKey('user.id'))
    user=db.relationship('User', backref=db.backref('surveys', lazy='dynamic'))
    def __init__(self, survey_name, uid):
        self.survey_name = survey_name
        self.user_name = uid

class Surveyquestion(db.Model):
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    questionName = db.Column(db.String(500), nullable = False)
    questionType = db.Column(db.String(500), nullable = False)
    survey_name = db.Column(db.Integer, db.ForeignKey('survey.id'))
    survey=db.relationship('Survey', backref=db.backref('questions', lazy='dynamic'))
    def __init__(self, questionName, questionType, surveyid):
        self.questionName = questionName
        self.questionType = questionType
        self.survey_name = surveyid

class Surveyquestionanswer(db.Model):
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    answerString = db.Column(db.String(500), nullable = False)
    surveyquestion_name = db.Column(db.Integer, db.ForeignKey('surveyquestion.id'))
    surveyquestion=db.relationship('Surveyquestion', backref=db.backref('answers', lazy='dynamic'))
    def __init__(self, ans, questionid):
        self.answerString = ans
        self.surveyquestion_name = questionid

class UserSurveyStates(db.Model):
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    questionState=db.Column(db.Integer, nullable=False) #0 => not asked 1 => previously asked 2 => never asked
    surveyId=db.Column(db.Integer, db.ForeignKey('survey.id'))
    questionId=db.Column(db.Integer, db.ForeignKey('question.id'))

