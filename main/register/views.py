# quiz/views.py
from flask import Blueprint
from flask_restful import Api
from main.register.resources import RegistrationResource 
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')

bp = Blueprint(config.get('Modules', 'REGISTER'), __name__)
api = Api(bp)

api.add_resource(RegistrationResource, config.get('API Paths', 'REGISTER'))



