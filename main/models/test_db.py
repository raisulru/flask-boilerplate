from main import db

# For Relational database when use SqlAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

# For NoSQL database when use flask-mongoengine
'''class User(db.Document):
    username = db.StringField()
    email = db.StringField()'''
