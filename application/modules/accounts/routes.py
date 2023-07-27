from flask import Blueprint, jsonify, request, abort
from bson.errors import InvalidId
from application.modules.accounts.services import (
    service_create_account, 
    service_get_account, 
    service_update_account, 
    service_delete_account
)
from application.modules.accounts.validators import validate_account
from application.utils.database import pymongo


accounts_bp = Blueprint("accounts", __name__, url_prefix="/accounts")


@accounts_bp.route("", methods=['POST'])
def create_account():
    try:
        data = request.json
        errors = validate_account(data)
        
        if errors:
            return jsonify(errors), 400

        account_id = service_create_account(data)
        return jsonify({"account_id": str(account_id)}), 201
    
    except pymongo.errors.ConnectionFailure:
        return jsonify({"error": "Database connection failed"}), 500



@accounts_bp.route("/<account_id>", methods=['GET'])
def get_account(account_id):
    try:
        account = service_get_account(account_id)
        if not account:
            abort(404, description="Account not found")
        
        # Convert ObjectId of the account (which is a BSON type) to a string so it can be serialized into JSON
        account["_id"] = str(account["_id"])
        return jsonify(account), 200

    # If account_id is not a valid BSON ObjectId
    except InvalidId:
        return jsonify({"error": "Invalid account ID format"}), 400
