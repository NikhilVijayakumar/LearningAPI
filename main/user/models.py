from main import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, userName, password, email):
        self.userName = userName
        self.email = email
        self.password = password
