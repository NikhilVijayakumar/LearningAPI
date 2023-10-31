# quiz/views.py
from flask import Blueprint
from config import ConfigSingleton
from main.register.resources import RegistrationResource 
import configparser

app = ConfigSingleton.get_app()
api = ConfigSingleton.get_api()

config = configparser.ConfigParser()
config.read('config.cfg')

bp = Blueprint(config.get('Modules', 'REGISTER'), __name__)
app.register_blueprint(bp)

api.add_resource(RegistrationResource, config.get('API Paths', 'REGISTER'))



