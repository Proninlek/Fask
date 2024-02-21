from sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    lastname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)

    def __repr__(self):
       return f"User({self.id}, {self.username}, {self.lastname}, {self.email}, {self.password})"