from main import db

class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    topic = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)

    def __init__(self, user_id, topic, type):
        self.user_id = user_id
        self.topic = topic
        self.type = type

class ChapterResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_result_id = db.Column(db.Integer, db.ForeignKey("quiz_result.id"), nullable=False)
    chapterName = db.Column(db.String(255))
    totalQuestions = db.Column(db.Integer)
    correctAnswers = db.Column(db.Integer)

    def __init__(self, quiz_result_id, chapterName, totalQuestions, correctAnswers):
        self.quiz_result_id = quiz_result_id
        self.chapterName = chapterName
        self.totalQuestions = totalQuestions
        self.correctAnswers = correctAnswers

