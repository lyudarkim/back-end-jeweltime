from marshmallow import Schema, fields


class AccountSchema(Schema):

    # account_id will only be used when serializing the object but not when loading (or deserializing) it
    account_id = fields.Integer(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    zipcode = fields.Int(required=True)