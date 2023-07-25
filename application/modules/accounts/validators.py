from marshmallow import fields, Schema, ValidationError

custom_errors = {
    "required": "{field_name} is required.",
    "invalid_email": "{field_name} must be a valid email."
}

class AccountSchema(Schema):
    # account_id is the ObjectId stored as a string
    # dump_only means that account_id will only be used when serializing the object but not when loading (or deserializing) it
    account_id = fields.String(dump_only=True)
    first_name = fields.Str(
        required=True,
        error_messages={
            "required": custom_errors["required"].format(field_name="First name")
        }
    )
    last_name = fields.Str(
        required=True,
        error_messages={
            "required": custom_errors["required"].format(field_name="Last name")
        }
    )
    email = fields.Email(
        required=True,
        error_messages={
            "required": custom_errors["required"].format(field_name="Email"),
            "invalid": custom_errors["invalid_email"].format(field_name="Email")
        }
    )
    zipcode = fields.Int(
        required=True,
        error_messages={
            "required": custom_errors["required"].format(field_name="Zipcode")
        }
    )