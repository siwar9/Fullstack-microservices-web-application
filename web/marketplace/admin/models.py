from email.policy import default
from marketplace import db, app, bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    profile = db.Column(db.String(150), unique=False, nullable=False, default='dummy_profile')


    def __repr__(self):
        return '<User %r>' % self.name
    

with app.app_context():
    db.create_all()
