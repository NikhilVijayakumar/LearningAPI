from flask import Blueprint
from main.quiz.resources import QuizResource
from main import api

quiz_bp = Blueprint("quiz", __name__)
api.add_resource(QuizResource, "/api/v1/quiz")