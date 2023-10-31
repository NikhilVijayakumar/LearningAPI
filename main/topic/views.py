# topic/views.py

from flask import Blueprint
from config import app,api
from main.topic.resources import TopicsResource
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')

bp = Blueprint(config.get('Modules', 'TOPIC'), __name__)
app.register_blueprint(bp)

api.add_resource(TopicsResource, config.get('API Paths', 'GET_TOPICS'))


