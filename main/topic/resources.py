from flask_restful import Resource
from flask import request, jsonify, send_from_directory
from waitress import serve
import os
import configparser
from flask_jwt_extended import jwt_required, get_jwt_identity

config = configparser.ConfigParser()
config.read('config.cfg')
quiz_data_path = config.get('App', 'QUIZ_DATA_PATH')

class TopicsResource(Resource):
    @jwt_required
    def get(self):
        response_data = {
            "status": "success",
            "data": None
        }

        topics = []

        for topic_folder in os.listdir(quiz_data_path):
            if os.path.isdir(os.path.join(quiz_data_path, topic_folder)):
                quiz_types = []
                topic_folder_path = os.path.join(quiz_data_path, topic_folder)
                for quiz_type_folder in os.listdir(topic_folder_path):
                    if os.path.isdir(os.path.join(topic_folder_path, quiz_type_folder)):
                        quiz_types.append(quiz_type_folder)

                topics.append({"name": topic_folder, "types": quiz_types})

        if topics:
            response_data["data"] = {"topics": topics}
        else:
            response_data["data"] = None
            return jsonify(response_data), 204

        return jsonify(response_data)


