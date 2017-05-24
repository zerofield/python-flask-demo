from user import User
from db import db
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
db.init_app(app)



db.create_all()

admin = User('admin', 'admin@example.com')
guest = User('guest', 'guest@example.com')


db.session.add(admin)
db.session.add(guest)
db.session.commit()

users = User.query.all()
print(users)

admin = User.query.filter_by(username='admin').first()
print(admin)



