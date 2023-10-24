from flask_jwt_extended import jwt_required
from flask_restful import Resource
from main.user.models import User
from main.user.schemas import UserSchema


users_schema = UserSchema(many=True)
user_schema = UserSchema()


class UserResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)


class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        return {"message": "You have access to this protected resource."}, 200
