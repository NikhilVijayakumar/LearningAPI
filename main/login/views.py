# login views.py
from flask import Blueprint
from config import app,api
from main.login.resources  import LoginResource 
import configparser


config = configparser.ConfigParser()
config.read('config.cfg')

bp = Blueprint(config.get('Modules', 'LOGIN'), __name__)
app.register_blueprint(bp)

api.add_resource(LoginResource, config.get('API Paths', 'LOGIN'))



