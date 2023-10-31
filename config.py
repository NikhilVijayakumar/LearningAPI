#config.py is used to configure the Flask app instance
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

class ConfigSingleton:
    app = None
    api = None
    db = None
    ma = None
    jwt = None

    @classmethod
    def get_app(cls):
        if cls.app is not None:
            return cls.app

        app = Flask(__name__)
        CORS(app)
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SECRET_KEY"] = "1c535e0f1083c66edecb9a3d8f16b907e58e5ebfc2b2b84535a8a7a9d9bf8888"

        cls.app = app
        return cls.app

    @classmethod
    def get_api(cls):
        if cls.api is None:
            cls.api = Api(cls.get_app())
        return cls.api

    @classmethod
    def get_db(cls):
        if cls.db is None:
            cls.db = SQLAlchemy(cls.get_app())
        return cls.db

    @classmethod
    def get_ma(cls):
        if cls.ma is None:
            cls.ma = Marshmallow(cls.get_app())
        return cls.ma

    @classmethod
    def get_jwt(cls):
        if cls.jwt is None:
            cls.jwt = JWTManager(cls.get_app())
        return cls.jwt




