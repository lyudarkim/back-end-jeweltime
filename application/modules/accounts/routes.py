from flask import Blueprint, jsonify, request, abort
from bson import ObjectId  
from bson.errors import InvalidId
from application.modules.accounts.services import (
    service_create_account, 
    service_get_account, 
    service_update_account, 
    service_delete_account
)
from application.modules.accounts.validators import validate_account
# from application.utils.database import pymongo
from pymongo.errors import ConnectionFailure


accounts_bp = Blueprint("accounts", __name__, url_prefix="/accounts")


@accounts_bp.route("", methods=['POST'])
def create_account():
    try:
        data = request.json
        errors = validate_account(data, partial=False)
        
        if errors:
            return jsonify(errors), 400
        
        # Fetch the whole account
        new_account = service_create_account(data)
        
        return jsonify(new_account), 201
    
    except ConnectionFailure:
        return jsonify({"error": "Database connection failed"}), 500


@accounts_bp.route("/<account_id>", methods=['GET'])
def get_account(account_id):
    try:
        account = service_get_account(account_id)
        if not account:
            abort(404, description="Account not found")
        
        account["account_id"] = str(account.pop("_id"))
        return jsonify(account), 200

    # If 'account_id' is not a valid BSON ObjectId
    except InvalidId:
        return jsonify({"error": "Invalid account ID format"}), 400


@accounts_bp.route("/<account_id>", methods=['PUT', 'PATCH'])
def update_account(account_id):
    try: 
        data = request.json
        errors = validate_account(data, partial=True)

        if errors:
            return jsonify(errors), 400

        count = service_update_account(account_id, data)
        
        if count == 0:
            abort(404, description="Account not found or not updated.")
        
        return jsonify({"message": "Account updated successfully"})
    
    except InvalidId:
            return jsonify({"error": "Invalid account ID format"}), 400
        
    except ConnectionFailure:
        return jsonify({"error": "Database connection failed"}), 500
    

@accounts_bp.route("/<account_id>", methods=['DELETE'])
def delete_account(account_id):
    try:
        count = service_delete_account(account_id)
        
        if count == 0:
            abort(404, description="Account not found.")
        
        return jsonify({"message": "Account deleted successfully"})
    
    except InvalidId:
        return jsonify({"error": "Invalid account ID format"}), 400
        
    except ConnectionFailure:
        return jsonify({"error": "Database connection failed"}), 500


