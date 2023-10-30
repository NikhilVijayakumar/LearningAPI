from config import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255), nullable=False)


class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    topic = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)

class ChapterResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_result_id = db.Column(db.Integer, db.ForeignKey("quiz_result.id"), nullable=False)
    chapterName = db.Column(db.String(255))
    totalQuestions = db.Column(db.Integer)
    correctAnswers = db.Column(db.Integer)