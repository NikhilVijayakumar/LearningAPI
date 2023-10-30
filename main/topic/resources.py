from flask_restful import Resource
from flask import request, jsonify, send_from_directory
from waitress import serve
import os
import json

quiz_data_path = "quiz_data"

class TopicsResource(Resource):
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

        return jsonify(response_data)

class QuizResource(Resource):
    def post(self):
        selected_topic = request.json.get("topic")
        selected_type = request.json.get("type")

        response_data = {
            "status": "success",
            "data": None
        }

        topic_folder_path = os.path.join(quiz_data_path, selected_topic)
        type_folder_path = os.path.join(topic_folder_path, selected_type)

        if not os.path.isdir(topic_folder_path) or not os.path.isdir(type_folder_path):
            response_data["status"] = "error"
            response_data["message"] = "Topic or type not found"
        else:
            quiz_files = [f for f in os.listdir(type_folder_path) if f.endswith(".json")]

            if quiz_files:
                quiz_file_path = os.path.join(type_folder_path, quiz_files[0])
                with open(quiz_file_path, "r") as json_file:
                    quiz_data = json.load(json_file)
                quiz_list = []
                for chapter_name, questions in quiz_data.items():
                    for question in questions:
                        question_option = {
                            "chaptername": chapter_name,
                            "question": question
                        }
                        quiz_list.append(question_option)
                response_data["data"] = quiz_list
            else:
                response_data["status"] = "error"
                response_data["message"] = "No quiz data found for the selected type"

        return jsonify(response_data)
