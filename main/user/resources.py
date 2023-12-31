from flask_jwt_extended import jwt_required
from flask_restful import Resource
from main.user.models import User
from main.user.schemas import UserListSchema






class UserResource(Resource):
    def get(self):
        user = User.query.order_by(User.id.desc())
        user_schema = UserListSchema(many=True)
        return {"data": user_schema.dump(user)}


