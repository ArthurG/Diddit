from diddit.models import User, Survey, Surveyquestion, Surveyquestionanswer
from diddit import *
from diddit.database import db
from diddit import diddit


arthur = User("100 King street west M5X 1E3", "bmo", "foo", "bar")

db.session.add(arthur)
db.session.commit()

survey = Survey("typical survey", arthur.id)
db.session.add(survey)
db.session.commit()

sQuestion = Surveyquestion("rate our service from 1-10", "rating", survey.id)
db.session.add(sQuestion)
db.session.commit()

ans = Surveyquestionanswer("5",  sQuestion.id)
db.session.add(ans)
db.session.commit()

print(survey.user)

