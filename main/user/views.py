from flask import Blueprint
from main.user.resources import ProtectedResource, UserResource
from main import api


user_bp = Blueprint("user", __name__)
api.add_resource(UserResource, "/api/v1/user")
api.add_resource(ProtectedResource, "/api/v1/user/protected")
