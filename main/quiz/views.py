# quiz/views.py
from flask import Blueprint
from main import api as Api
from main.quiz.resources import QuizResource 
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')

bp = Blueprint(config.get('Modules', 'QUIZ'), __name__)
api = Api(bp)

api.add_resource(QuizResource, config.get('API Paths', 'GET_QUIZ'))
