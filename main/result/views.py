# result/views.py
from flask import Blueprint
from flask_restful import Api
from main.result.resources import SaveResultsResource, GetResultsResource
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')

bp = Blueprint(config.get('Modules', 'RESULT'), __name__)
api = Api(bp)

api.add_resource(SaveResultsResource,  config.get('API Paths', 'SAVE_RESULTS'))
api.add_resource(GetResultsResource, config.get('API Paths', 'GET_RESULTS'))
