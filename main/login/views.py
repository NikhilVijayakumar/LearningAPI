# login views.py
from flask import Blueprint
from flask_restful import Api
from main.login.resources  import LoginResource 
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')

bp = Blueprint(config.get('Modules', 'LOGIN'), __name__)
api = Api(bp)

api.add_resource(LoginResource, config.get('API Paths', 'LOGIN'))


