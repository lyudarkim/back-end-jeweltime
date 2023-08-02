from marshmallow import fields, Schema, ValidationError
from marshmallow.validate import Length
from application.utils.helpers import validate_not_empty_or_whitespace


class AccountSchema(Schema):
    # accountId is the ObjectId stored as a string.
    # dump_only means that accountId will only be used when serializing
    # the object but not when loading (or deserializing) it.
    accountId = fields.Str(dump_only=True)
    
    firstName = fields.Str(
        required=True,
        validate=validate_not_empty_or_whitespace,
        error_messages={
            "required": "First name is required."
        }
    )
    
    lastName = fields.Str(
        required=True,
        validate=validate_not_empty_or_whitespace,
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
            validate_not_empty_or_whitespace
        ],
        error_messages={
            "required": "Zipcode is required."
        }
    )


def validate_account(data, partial=False):
    """Validates account data against the AccountSchema."""
    schema = AccountSchema()
    schema.load(data, partial=partial)

