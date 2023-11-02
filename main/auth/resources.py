from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from main.user.models import User
import re
from main import db


class RegistrationResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "userName", type=str, required=True, help="userName is required."
        )
        parser.add_argument("email", type=str, required=True, help="Email is required.")
        parser.add_argument(
            "password", type=str, required=True, help="Password is required."
        )
        args = parser.parse_args()

        userName = args["userName"]
        email = args["email"]
        password = args["password"]

        if User.query.filter_by(userName=userName).first():
            return {"message": "userName already exists."}, 400

        if User.query.filter_by(email=email).first():
            return {"message": "Email already exists."}, 400

        if not self.is_valid_email(email):
            return {"message": "Invalid email format."}, 400

        if not self.is_valid_password(password):
            return {"message": "Invalid password format."}, 400

        user = User(userName=userName, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        return {"message": "User registered successfully."}, 201

    def is_valid_email(self, email):
        allowed_domains = ["opentrends.net", "seidoropentrends.com"]
        domain = email.split("@")[1] if "@" in email else ""
        return domain in allowed_domains

    def is_valid_password(self, password):
        password_regex = re.compile(
            r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)(?!.*\s).{8,50}$"
        )
        return bool(re.match(password_regex, password))


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

        access_token = create_access_token(identity=user.id,expires_delta=False)
        return {"data":{"user": {"token": access_token, "userName" : user.userName , "email" : user.email}}}, 200
