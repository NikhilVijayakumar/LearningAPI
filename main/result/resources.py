# result/resources.py
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from db_schema import User,db,QuizResult,ChapterResult

class SaveResultsResource(Resource):
    @jwt_required
    def post(self):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)

        data = request.get_json()
        topic = data["data"]["topic"]
        exam_type = data["data"]["type"]

        quiz_result = QuizResult(user_id=user.id, topic=topic, type=exam_type)

        for chapter_result_data in data["data"]["chapterResults"]:
            chapter_result = ChapterResult(
            quiz_result=quiz_result,
            chapterName=chapter_result_data["chapterName"],
            totalQuestions=chapter_result_data["totalQuestions"],
            correctAnswers=chapter_result_data["correctAnswers"]
            )
            db.session.add(chapter_result)

        db.session.commit()

        return jsonify({"data": {"topic": topic, "type": exam_type, "chapterResults": data["data"]["chapterResults"]}}), 201



class GetResultsResource(Resource):
    @jwt_required
    def get(self):
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