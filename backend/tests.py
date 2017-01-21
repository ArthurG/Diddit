from diddit.models import User
from diddit import db

arthur = User("100 King street west M5X 1E3", "bmo", "foo", "bar")

db.session.add(arthur)
db.session.commit()

users = User.query.all()
print(users)

