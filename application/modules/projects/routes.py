from flask import Blueprint, jsonify, request, abort
from bson.errors import InvalidId
from application.modules.accounts.services import service_create_account
from application.modules.projects.services import (
    service_create_project, 
    # service_get_project, 
    # service_update_project, 
    # service_delete_project
)
from application.modules.projects.validators import validate_project
from application.utils.database import pymongo
from pymongo.errors import ConnectionFailure


projects_bp = Blueprint("projects", __name__, url_prefix="/accounts/<account_id>/projects")


@projects_bp.route("", methods=['POST'])
def create_project(account_id):
    try:
        data = request.json
        errors = validate_project(data, partial=False)
        
        if errors:
            return jsonify(errors), 400

        project_id = service_create_project(data, account_id)
        return jsonify({"project_id": str(project_id)}), 201
    
    except ConnectionFailure:
        return jsonify({"error": "Database connection failed"}), 500
