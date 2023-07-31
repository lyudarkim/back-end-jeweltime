from flask import Blueprint, jsonify, request, abort
from application.modules.projects.services import (
    service_create_project, 
    service_get_project, 
    service_get_all_projects,
    service_update_project, 
    # service_delete_project
)
from application.modules.projects.validators import validate_project
from application.utils.helpers import handle_errors


projects_bp = Blueprint("projects", __name__, url_prefix="/projects")
get_all_projects_bp = Blueprint("projects_for_account", __name__, url_prefix="/accounts/<accountId>/projects")


@projects_bp.route("", methods=['POST'])
@handle_errors
def create_project():
    data = request.json
    errors = validate_project(data, partial=False)
    
    if errors:
        return jsonify(errors), 400

    new_project = service_create_project(data)
    
    return jsonify(new_project), 201


@projects_bp.route("/<projectId>", methods=['GET'])
@handle_errors
def get_project(projectId):
    project = service_get_project(projectId)

    return jsonify(project), 200


@get_all_projects_bp.route("", methods=['GET'])
@handle_errors
def get_all_projects(accountId):
    all_projects = service_get_all_projects(accountId)

    return jsonify(all_projects), 200


@projects_bp.route("/<projectId>", methods=['PUT', 'PATCH'])
@handle_errors
def update_project(accountId, projectId):
    data = request.json
    errors = validate_project(data, partial=True)
    
    if errors:
        return jsonify(errors), 400
    
    updated_project = service_update_project(projectId, accountId, data)

    return jsonify(updated_project), 200