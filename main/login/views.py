from flask import Blueprint
from main.login.resources import LoginResource
from main import api


login_bp = Blueprint("login", __name__)
api.add_resource(LoginResource, "/api/v1/login")
