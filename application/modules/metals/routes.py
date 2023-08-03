from flask import Blueprint, jsonify
from application.modules.metals.services import service_get_metal_prices
from application.utils.helpers import handle_errors


metals_bp = Blueprint("metals", __name__)


@metals_bp.route("/prices", methods=['GET'])
@handle_errors
def get_metal_prices():
    metal_prices = service_get_metal_prices()
    
    return jsonify(metal_prices), 200
