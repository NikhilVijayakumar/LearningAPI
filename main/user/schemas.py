from main import ma
from main.user.models import User


class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ("userName", "email", "password")
