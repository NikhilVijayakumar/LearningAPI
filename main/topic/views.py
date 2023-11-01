from flask import Blueprint
from main.topic.resources import TopicsResource
from main import api

topic_bp = Blueprint("topic", __name__)
api.add_resource(TopicsResource, "/api/v1/topics")
