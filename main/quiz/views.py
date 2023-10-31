# quiz/views.py
from flask import Blueprint
from config import app,api
from main.quiz.resources import QuizResource 
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')

bp = Blueprint(config.get('Modules', 'QUIZ'), __name__)
app.register_blueprint(bp)

api.add_resource(QuizResource, config.get('API Paths', 'GET_QUIZ'))
