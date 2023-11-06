# __init__.py

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from waitress import serve
from flask_cors import CORS

# Create Flask app instance
app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://SkillSage:Apiskillsage#123@172.28.0.2:5432/Skillsage_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "your_secret_key"


# Initialize Flask extensions
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)


# Import and register blueprints
from main.user.views import user_bp
from main.auth.views import auth_bp
from main.topic.views import api_bp

# Register the file_bp blueprint
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(api_bp)

