from flask import Blueprint, jsonify, request
from application.modules.accounts.services import (
    service_create_account, 
    service_get_account, 
    service_get_account_by_firebase_id,
    service_update_account, 
    service_delete_account
)
from application.modules.accounts.validators import validate_account
from application.utils.helpers import handle_errors


accounts_bp = Blueprint("accounts", __name__, url_prefix="/accounts")
signin_bp = Blueprint("signin", __name__, url_prefix="/signin")


@accounts_bp.route("", methods=['POST'])
@handle_errors
def create_account():
    data = request.json
    validate_account(data, partial=False)
    new_account = service_create_account(data)
    
    return jsonify(new_account), 201


@accounts_bp.route("/<accountId>", methods=['GET'])
@handle_errors
def get_account(accountId):
    account = service_get_account(accountId)

    return jsonify(account), 200


@signin_bp.route("", methods=["POST"])
@handle_errors
def get_account_by_firebase_id():
    data = request.json
    firebase_id = data.get("firebaseId")

    if not firebase_id:
        return jsonify({
            "error": "Missing 'firebaseId' in request body"
        }), 400

    account = service_get_account_by_firebase_id(firebase_id)

    return jsonify(account), 200


@accounts_bp.route("/<accountId>", methods=['PUT', 'PATCH'])
@handle_errors
def update_account(accountId):
    data = request.json
    validate_account(data, partial=True)
    updated_account = service_update_account(accountId, data)
    
    return jsonify(updated_account), 200


@accounts_bp.route("/<accountId>", methods=['DELETE'])
@handle_errors
def delete_account(accountId):
    service_delete_account(accountId)
    
    return jsonify({
        "message": "Account and its projects deleted successfully"
    })


