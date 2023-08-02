from bson.errors import InvalidId
from flask import jsonify
from functools import wraps
import logging
from marshmallow import ValidationError
import requests
from werkzeug.exceptions import HTTPException  
from pymongo.errors import ConnectionFailure


def validate_not_empty_or_whitespace(data):
    """This function ensures that the provided data isn't just whitespace or empty."""
    if not data or data.strip() == "":
        raise ValidationError("Field cannot be empty or consist solely of whitespace.")


def handle_errors(function):
    """
    This is a higher-order function used as a decorator to catch and handle exceptions for accounts and projects route functions.
    It returns appropriate JSON responses for errors, logging unexpected ones.

    Parameters:
    - function: The function representing a Flask route to enhance with error handling.

    Returns:
    - A new function that handles errors and wraps around the original Flask route.
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)

        # Specific exceptions first
        except InvalidId:
            return jsonify({
                "error": "Invalid ID format"
            }), 400

        except ConnectionFailure:
            return jsonify({
                "error": "Database connection failed"
            }), 500
        
        # Handle schema validation errors from Marshmallow
        except ValidationError as e:  
            return jsonify({
                "error": e.messages
            }), 400

        # Flask's HTTPException (like abort())
        except HTTPException as e:  
            return jsonify({
                "error": e.description
            }), e.code
        
        # Handle errors from failed external API calls
        except requests.RequestException as e:
            return jsonify({
                "error": f"Error fetching metal prices: {str(e)}"
            }), 503  

        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        
        # General exception for unexpected errors
        except Exception:
            # Log the full error to diagnose issues in production
            logging.error("An unexpected error occurred", exc_info=True)

            # But return only a generic error message to the user
            return jsonify({
                "error": "An unexpected error occurred"
            }), 500
    
    return wrapper
