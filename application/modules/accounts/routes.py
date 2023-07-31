from flask import Blueprint, jsonify, request, abort
from application.modules.accounts.services import (
    service_create_account, 
    service_get_account, 
    service_update_account, 
    service_delete_account
)
from application.modules.accounts.validators import validate_account
from application.utils.helpers import handle_errors


accounts_bp = Blueprint("accounts", __name__, url_prefix="/accounts")


@accounts_bp.route("", methods=['POST'])
@handle_errors
def create_account():
    data = request.json
    errors = validate_account(data, partial=False)
    
    if errors:
        return jsonify(errors), 400
    
    new_account = service_create_account(data)
    
    return jsonify(new_account), 201


@accounts_bp.route("/<accountId>", methods=['GET'])
@handle_errors
def get_account(accountId):
    account = service_get_account(accountId)

    if not account:
        abort(404, description="Account not found")
    
    return jsonify(account), 200


@accounts_bp.route("/<accountId>", methods=['PUT', 'PATCH'])
@handle_errors
def update_account(accountId):
    data = request.json
    errors = validate_account(data, partial=True)

    if errors:
        return jsonify(errors), 400

    updated_account = service_update_account(accountId, data)
    
    if not updated_account:
        abort(404, description="Account not found or not updated.")
    
    return jsonify(updated_account), 200


@accounts_bp.route("/<accountId>", methods=['DELETE'])
@handle_errors
def delete_account(accountId):
    deleted_count = service_delete_account(accountId)

    if deleted_count == 0:
        abort(404, description="Account not found.")
    
    return jsonify({
        "message": "Account and its projects deleted successfully"
    })
