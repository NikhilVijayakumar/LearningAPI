# __init__.py

from flask_restful import Api
from config import app
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from main.login.views import bp as login_bp
from main.register.views import bp as register_bp
from main.topic.views import bp as topic_bp
from main.quiz.views import bp as quiz_bp
from main.result.views import bp as result_bp

# Initialize Flask extensions
api = Api(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

# Register the file_bp blueprint
app.register_blueprint(topic_bp)
app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(quiz_bp)
app.register_blueprint(result_bp)

