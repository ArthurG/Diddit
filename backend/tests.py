from diddit import db
from diddit.models import User
arthur = User("100 King street west M5X 1E3", "foo", "bar")

db.session.add(arthur)
db.session.commit()

users = User.query.all()
print(users)

