from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from main.user.models import User
import re
from main import db

class LoginResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", type=str, required=True, help="Email is required.")
        parser.add_argument(
            "password", type=str, required=True, help="Password is required."
        )
        args = parser.parse_args()

        email = args["email"]
        password = args["password"]

        user = User.query.filter_by(email=email).first()

        if not user or not user.password == password:
            return {"message": "Invalid credentials."}, 401

        access_token = create_access_token(identity=user.id)
        return {"data":{"user": {"token": access_token, "userName" : user.userName , "email" : user.email}}}, 200
