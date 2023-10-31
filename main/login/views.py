# login views.py
from flask import Blueprint
from config import ConfigSingleton
from main.login.resources  import LoginResource 
import configparser

app = ConfigSingleton.get_app()
api = ConfigSingleton.get_api()
config = configparser.ConfigParser()
config.read('config.cfg')

bp = Blueprint(config.get('Modules', 'LOGIN'), __name__)
app.register_blueprint(bp)

api.add_resource(LoginResource, config.get('API Paths', 'LOGIN'))



