from flask import Blueprint, jsonify, request, abort
# from bson import ObjectId  
from bson.errors import InvalidId
from application.modules.accounts.services import (
    service_create_account, 
    service_get_account, 
    service_update_account, 
    service_delete_account
)
from application.modules.accounts.validators import validate_account
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
        return jsonify({
            "error": "Database connection failed"
        }), 500


@accounts_bp.route("/<accountId>", methods=['GET'])
def get_account(accountId):
    try:
        account = service_get_account(accountId)
        if not account:
            abort(404, description="Account not found")
        
        return jsonify(account), 200

    # If 'accountId' is not a valid BSON ObjectId
    except InvalidId:
        return jsonify({
            "error": "Invalid account ID format"
        }), 400


@accounts_bp.route("/<accountId>", methods=['PUT', 'PATCH'])
def update_account(accountId):
    try: 
        data = request.json
        errors = validate_account(data, partial=True)

        if errors:
            return jsonify(errors), 400

        account = service_update_account(accountId, data)
        
        if not account:
            abort(404, description="Account not found or not updated.")
        
        return jsonify({
            "account": account, 
            "message": "Account updated successfully"
        })
    
    except InvalidId:
            return jsonify({"error": "Invalid account ID format"}), 400
        
    except ConnectionFailure:
        return jsonify({"error": "Database connection failed"}), 500
    

@accounts_bp.route("/<accountId>", methods=['DELETE'])
def delete_account(accountId):
    try:
        count = service_delete_account(accountId)
        
        if count == 0:
            abort(404, description="Account not found.")
        
        return jsonify({"message": "Account deleted successfully"})
    
    except InvalidId:
        return jsonify({"error": "Invalid account ID format"}), 400
        
    except ConnectionFailure:
        return jsonify({"error": "Database connection failed"}), 500


