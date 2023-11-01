from flask import Blueprint
from main.result.resources import SaveResultsResource, GetResultsResource
from main import api



result_bp = Blueprint("result", __name__)
api.add_resource(SaveResultsResource, "/api/v1/results")
api.add_resource(GetResultsResource, "/api/v1/result")
