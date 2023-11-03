from main import ma
from main.user.models import User


class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ("user_name", "email", "password")


class UserListSchema(UserSchema):
    class Meta:
        fields = ("user_name", "email")