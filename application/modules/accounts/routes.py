from flask import Blueprint, jsonify, request


accounts_bp = Blueprint("accounts", __name__, url_prefix="/accounts")


@accounts_bp.route("", methods=['GET'])
def get_accounts():
    return "Hello Accounts!"