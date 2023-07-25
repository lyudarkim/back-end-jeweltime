from marshmallow import fields, Schema, ValidationError
from marshmallow.validate import Length
from application.utils.helpers import validate_not_only_whitespace


class AccountSchema(Schema):
    # account_id is the ObjectId stored as a string.
    # dump_only means that account_id will only be used when serializing
    # the object but not when loading (or deserializing) it.
    account_id = fields.String(dump_only=True)
    
    first_name = fields.Str(
        required=True,
        validate=[
            Length(min=1, error="Field cannot be empty."),
            validate_not_only_whitespace
        ],
        error_messages={
            "required": "First name is required."
        }
    )
    
    last_name = fields.Str(
        required=True,
        validate=[
            Length(min=1, error="Field cannot be empty."),
            validate_not_only_whitespace
        ],
        error_messages={
            "required": "Last name is required."
        }
    )
    
    email = fields.Email(
        required=True,
        error_messages={
            "required": "Email is required.",
        }
    )
    
    # Storing zipcodes as strings in case there are international users.
    zipcode = fields.Str(
        required=True,
        validate=[
            Length(min=3, max=10),
            validate_not_only_whitespace
        ],
        error_messages={
            "required": "Zipcode is required."
        }
    )


def validate_account(data):
    """Validates account data against the AccountSchema."""
    schema = AccountSchema()
    try:
        validated_data = schema.load(data)
        return validated_data
    except ValidationError as error:
        return error.messages
