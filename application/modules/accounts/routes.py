from flask import Blueprint, jsonify, request, abort
from application.modules.accounts.services import (
    service_create_account, 
    service_get_account, 
    service_update_account, 
    service_delete_account
)
from application.modules.accounts.validators import validate_account


accounts_bp = Blueprint("accounts", __name__, url_prefix="/accounts")


# @accounts_bp.route("", methods=['GET'])
# def get_accounts():
#     return "Hello Accounts!"

@accounts_bp.route("", methods=['POST'])
def create_account():
    data = request.json
    errors = validate_account(data)
    
    if errors:
        return jsonify(errors), 400

    account_id = service_create_account(data)

    return jsonify({"account_id": str(account_id)}), 201


