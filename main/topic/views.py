# topic/views.py

from flask import Blueprint
from flask_restful import Api
from main.topic.resources import TopicsResource
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')

bp = Blueprint(config.get('Modules', 'TOPIC'), __name__)
api = Api(bp)

api.add_resource(TopicsResource, config.get('API Paths', 'GET_TOPICS'))


