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
    total_questions = db.Column(db.Integer)
    correct_answers = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'quizId': self.quiz_id,
            'topic': self.topic,
            'type': self.type,
            'totalQuestions': self.total_questions,
            'correctAnswers': self.correct_answers,
        }

class ChapterResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_result_id = db.Column(db.String(255), db.ForeignKey("quiz_result.quiz_id"), nullable=False)
    chapter_name = db.Column(db.String(255))
    total_questions = db.Column(db.Integer)
    correct_answers = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'quizResultId': self.quiz_result_id,
            'chapterName': self.chapter_name,
            'totalQuestions': self.total_questions,
            'correctAnswers': self.correct_answers,
        }

@app.route("/api/v1/results", endpoint='get_quiz_results', methods=["GET"])
@jwt_required()
def get_quiz_results():
    topic = request.args.get("topic")
    exam_type = request.args.get("type")
    user_id = request.args.get("userId")

    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user and not user_id:
        return jsonify({"message": "User not found"}), 404

    if user_id:
        user = User.query.get(user_id)
    
    

    if topic and exam_type:
        quiz_result = QuizResult.query.filter_by(user_id=user.id, topic=topic, type=exam_type).all()
    elif topic:
        quiz_result = QuizResult.query.filter_by(user_id=user.id, topic=topic).all()
    elif exam_type:
        quiz_result = QuizResult.query.filter_by(user_id=user.id, type=exam_type).all()
    else:
        quiz_result = QuizResult.query.filter_by(user_id=user.id).all()
    

    if not quiz_result:
        return jsonify({"message": "QuizResult not found for user "}), 404

    quiz_data = []

    for result in quiz_result:
        result_data = []
        chapter_results_list = ChapterResult.query.filter_by(quiz_result_id=result.quiz_id).all()
        chapter_results_data = [chapter_result.to_dict() for chapter_result in chapter_results_list]
        if not chapter_results_data:
            return jsonify({"message": "ChapterResult not found"}), 404

        result_data.append({
            "topic": result.topic,
            "type": result.type,
            "totalQuestions": result.total_questions,
            "correctAnswers": result.correct_answers,
            "chapterResults": chapter_results_data
        })
        quiz_data.append({
            "quizId": result.quiz_id,
            "data": result_data
        })

    return jsonify({"quiz": quiz_data})



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
    total_questions=data["data"]["totalQuestions"]
    correct_answers=data["data"]["correctAnswers"]
    quiz_id = str(uuid.uuid4())
    quiz_result = QuizResult(user_id=user.id,quiz_id=quiz_id, topic=topic, type=exam_type,total_questions=total_questions,correct_answers=correct_answers)
    db.session.add(quiz_result)

    for chapter_result_data in chapter_results:
        chapter_result = ChapterResult(
            quiz_result_id=quiz_id,
            chapter_name=chapter_result_data.get("chapterName"),
            total_questions=chapter_result_data.get("totalQuestions"),
            correct_answers=chapter_result_data.get("correctAnswers")
        )
        db.session.add(chapter_result)

    db.session.commit()
    return jsonify({"message": "Quiz Result saved successfully"}), 201


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    serve(app, host="0.0.0.0", port=5000)
