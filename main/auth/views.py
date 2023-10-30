from flask import Blueprint
from main.auth.resources import LoginResource, RegistrationResource
from main import api


auth_bp = Blueprint("auth", __name__)
api.add_resource(LoginResource, "/auth/login")
api.add_resource(RegistrationResource, "/auth/register")
