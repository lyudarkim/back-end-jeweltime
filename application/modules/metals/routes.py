from flask import Blueprint, jsonify, request
from application.modules.metals.services import get_metal_prices
from application.utils.helpers import handle_errors


metals_bp = Blueprint("metals", __name__, url_prefix="/metals")


@metals_bp.route("/prices", methods=['GET'])
@handle_errors
def prices():
    metal_prices = get_metal_prices()
    
    return jsonify(metal_prices), 200
