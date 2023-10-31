#config.py is used to configure the Flask app instance
from flask import Flask
from flask_cors import CORS
from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
    
# Create Flask app instance
app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] ="1c535e0f1083c66edecb9a3d8f16b907e58e5ebfc2b2b84535a8a7a9d9bf8888"

# Initialize Flask extensions
api = Api(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

