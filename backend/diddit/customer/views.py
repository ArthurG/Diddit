from flask import request
import sys
from ..models import Survey
from ..models import Surveyquestion
from ..models import Surveyquestionanswer
from ..models import User
from flask_sqlalchemy import SQLAlchemy
import json 
import requests
from . import customer
from database import db



@customer.route('/login', methods=['POST'])
def login():
	print("loggin in")

	# endpoint for processing incoming messaging events
	data = request.get_json(force=True)
	log("incoming msg " + str(data))

	userName = data['username']
	passWord = data['password']

	Users = User.query.all() # .filter(User.username == userName)

	Users = [i for i in Users if i.username == userName]

	for aUser in Users:
		if aUser.password == passWord:
			return "ok", 200

	return "unauthorized", 401 


# return json of answers to each question  
@customer.route('/answers', methods=['GET'])
def answers():
	data = request.get_json(force=True)
	#


# return json which contains survey questions 
@customer.route('/survey', methods=['GET'])
def survey():
	data = request.get_json(force=True)
	#



'''
{
  "surveyname": "Test1",
  "uid": "123",
  "questions": [
	{
	  "question": "rate our service from 1-10",
	  "type": "r"
	},
	{
	  "question": "Do you like boys or girls? a: boys; b: girls; c: neither; d: both" ,
	  "type": "m"
	},
	{
	  "question": "Any comments?",
	  "type": "s"
	}
  ]
}

'''
# add the questions to db using survey id
@customer.route('/survey', methods=['POST'])
def surveys():
	data = request.get_json(force=True)
	log("incoming msg " + str(data))  # you may not want to log every incoming message in production, but it's good for testing
	# print (data['questions'])
	# endpoint for signups 	('surveyname' in data) and ('uid' in data):

	if( 'username' in data ) and ( 'surveyname' in data ):

		Users = User.query.all()
		Users = [i for i in Users if i.username == userName]

		surveyID = Users[0].id

		name = data['surveyname']
		
		tempSurvey = Survey(name, surveyID)
		sID = tempSurvey.id
		db.session.add(tempSurvey)
		db.session.commit()

		if ('questions' in data):
			for q in data['questions']:
				tempQuestion = q['question']
				tempType = q['type']
				Surveyquestion(tempQuestion, tempType, sID)

	
	

	return "ok", 200 




'''
{
  "location": "40 St George St, Toronto, ON M5S 2E4",
  "storename": "777",
  "username": "Harman",
  "password": "Gay"
}
'''
@customer.route('/signup', methods=['POST'])
def signup():
	# endpoint for processing incoming messaging events
	data = request.get_json(force=True)
	log("incoming msg " + str(data))  # you may not want to log every incoming message in production, but it's good for testing

	# endpoint for signups
	if ('location' in data) and ('storename' in data) and ('username' in data) and ('password' in data):
		location = data['location']
		storename = data['storename']
		userName = data['username']
		password = data['password']
		
		
		Users = User.query.all()

		Users = [i for i in Users if i.username == userName]

		for aUser in Users:
			if (aUser.username == userName) and (aUser.store_name == storename):
				return "user already registered", 400
		
		temp = User(location, storename, userName, password)
		db.session.add(temp)
		db.session.commit()
		return "ok", 200


def log(message):  # simple wrapper for logging to stdout on heroku
	print(str(message))
	sys.stdout.flush()
