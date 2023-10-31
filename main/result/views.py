# result/views.py
from flask import Blueprint
from config import ConfigSingleton
from main.result.resources import SaveResultsResource, GetResultsResource
import configparser

app = ConfigSingleton.get_app()
api = ConfigSingleton.get_api()

config = configparser.ConfigParser()
config.read('config.cfg')

bp = Blueprint(config.get('Modules', 'RESULT'), __name__)
app.register_blueprint(bp)

api.add_resource(SaveResultsResource,  config.get('API Paths', 'SAVE_RESULTS'))
api.add_resource(GetResultsResource, config.get('API Paths', 'GET_RESULTS'))
