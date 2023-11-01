from flask import Blueprint
from main.registration.resources import  RegistrationResource
from main import api


register_bp = Blueprint("register", __name__)
api.add_resource(RegistrationResource, "/api/v1/register")
