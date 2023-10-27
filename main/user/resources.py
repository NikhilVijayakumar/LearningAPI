from flask_jwt_extended import jwt_required
from flask_restful import Resource
from main.user.models import User
from main.user.schemas import UserSchema
from marshmallow import Schema, fields

class UserListSchema(UserSchema):
    class Meta:
        fields = ("userName", "email")

users_list_schema = UserListSchema(many=True)

class UserResource(Resource):
    def get(self):
        users = User.query.all()
        return {"data": users_list_schema.dump(users)}

class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        return {"message": "You have access to this protected resource."}, 200
