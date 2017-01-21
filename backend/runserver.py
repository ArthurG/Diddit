import os
from diddit import diddit
from diddit.database import db
from flask import Flask

def runserver():
    diddit.run()

if __name__ == '__main__':
    runserver()
