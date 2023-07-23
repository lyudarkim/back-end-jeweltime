from flask import Blueprint, jsonify, request


projects_bp = Blueprint("projects", __name__, url_prefix="/projects")


@projects_bp.route("", methods=['GET'])
def get_projects():
    return "Hello Projects!"