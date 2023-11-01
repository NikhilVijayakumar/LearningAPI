from main import ma
from main.result.models import QuizResult, ChapterResult


class QuizResultSchema(ma.Schema):
    class Meta:
        model = QuizResult
        fields = ("user_id", "topic", "type")

class ChapterResultSchema(ma.Schema):
    class Meta:
        model = ChapterResult
        fields = ("quiz_result_id", "chapterName", "totalQuestions", "correctAnswers ")