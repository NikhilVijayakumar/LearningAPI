# app.py

from main import app, db
from waitress import serve
import os
import json
from flask import Flask, jsonify, request, abort, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.user.models import User
import uuid

class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    quiz_id = db.Column(db.String(255), nullable=False,unique=True)
    topic = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)

class ChapterResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_result_id = db.Column(db.String(255), db.ForeignKey("quiz_result.quiz_id"), nullable=False)
    chapterName = db.Column(db.String(255))
    totalQuestions = db.Column(db.Integer)
    correctAnswers = db.Column(db.Integer)

@app.route("/api/v1/results",  endpoint='get_quiz_results', methods=["GET"])
@jwt_required()
def get_quiz_results():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    results = QuizResult.query.filter_by(user_id=user.id).all()

    result_data = []
    for result in results:
        chapter_results = result.chapter_results
        chapter_results_data = [
            {
                "chapterName": chapter_result.chapterName,
                "totalQuestions": chapter_result.totalQuestions,
                "correctAnswers": chapter_result.correctAnswers
            }
            for chapter_result in chapter_results
        ]
        result_data.append({
            "topic": result.topic,
            "type": result.type,
            "chapterResults": chapter_results_data
        })

    return jsonify({"data": result_data})

@app.route('/api/v1/results', endpoint='save_results', methods=['POST']) 
@jwt_required()
def save_results():
    data = request.get_json()   
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)      
    if data is None:
        return jsonify({"message": "Invalid JSON data format"}), 400
        
    topic = data["data"]["topic"]
    exam_type = data["data"]["type"]
    chapter_results = data["data"]["chapterResults"]
    quiz_id = str(uuid.uuid4())
    quiz_result = QuizResult(user_id=user.id,quiz_id=quiz_id, topic=topic, type=exam_type)
    db.session.add(quiz_result)

    for chapter_result_data in chapter_results:
        chapter_result = ChapterResult(
            quiz_result_id=quiz_id,
            chapterName=chapter_result_data.get("chapterName"),
            totalQuestions=chapter_result_data.get("totalQuestions"),
            correctAnswers=chapter_result_data.get("correctAnswers")
        )
        db.session.add(chapter_result)

    db.session.commit()

    return jsonify({"data": {"topic": topic, "type": exam_type, "chapterResults": chapter_results}}), 201


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    serve(app, host="0.0.0.0", port=5000)
