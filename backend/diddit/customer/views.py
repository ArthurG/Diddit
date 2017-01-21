from flask import request
import sys
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

    Users = User.query.all().filter(User.username == userName)

    for aUser in Users:
    	if aUser.password == passWord:
    		return "ok", 200

    return "unauthorized", 401 



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
    	
    	Users = User.query.all().filter(User.username == userName)
    	for aUser in Users:
    		if (aUser.username == userName) and (aUser.storename == storename):
    			return "user already registered", 400
		
    	temp = User(location, storename, userName, password)
    	db.session.add(temp)
    	db.session.commit()
    	return "ok", 200


def log(message):  # simple wrapper for logging to stdout on heroku
    print(str(message))
    sys.stdout.flush()
