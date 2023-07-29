from flask import Blueprint, jsonify, request, abort
from bson.errors import InvalidId
from application.modules.accounts.services import service_create_account
from application.modules.projects.services import (
    service_create_project, 
    service_get_project, 
    # service_update_project, 
    # service_delete_project
)
from application.modules.projects.validators import validate_project
from application.utils.database import pymongo
from pymongo.errors import ConnectionFailure


projects_bp = Blueprint("projects", __name__, url_prefix="/accounts/<accountId>/projects")


@projects_bp.route("", methods=['POST'])
def create_project(accountId):
    try:
        data = request.json
        errors = validate_project(data, partial=False)
        
        if errors:
            return jsonify(errors), 400

        project = service_create_project(data, accountId)
        return jsonify(project), 201
    
    except ConnectionFailure:
        return jsonify({"error": "Database connection failed"}), 500


@projects_bp.route("/<projectId>", methods=['GET'])
def get_project(accountId, projectId):
    try:
        project = service_get_project(projectId, accountId)
        if not project:
            abort(404, description="Project not found")
        
        # Convert MongoDB ObjectIds to strings
        project["_id"] = str(project["_id"])
        project["accountId"] = str(project["accountId"])

        return jsonify(project), 200
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 404