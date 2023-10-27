from flask import Blueprint
from main.topic.resources import TopicsResource, QuizResource
from main import api

api_bp = Blueprint("api", __name__)
api.add_resource(TopicsResource, "/api/v1/topics")
api.add_resource(QuizResource, "/api/v1/quiz")


