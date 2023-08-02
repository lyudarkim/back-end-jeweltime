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
    validate_account(data, partial=False)
    new_account = service_create_account(data)
    
    return jsonify(new_account), 201


@accounts_bp.route("/<accountId>", methods=['GET'])
@handle_errors
def get_account(accountId):
    account = service_get_account(accountId)

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
