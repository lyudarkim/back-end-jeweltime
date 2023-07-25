from marshmallow import fields, Length, Schema, ValidationError

custom_errors = {
    "required": "{field_name} is required.",
    "invalid_length": "{field_name} exceeds the maximum length."
}


class ProjectSchema(Schema):
    # Using ObjectId which is a hex string
    account_id = fields.String(
        required=True,
        error_messages={
            "required": custom_errors["required"].format(field_name="Account ID")
        }
    )
    project_id = fields.String(dump_only=True)
    project_name = fields.Str(
        required=True,
        error_messages={
            "required": custom_errors["required"].format(field_name="Project name")
        }
    )
    description = fields.Str(
        required=True, 
        validate=Length(max=300),
        error_messages={
            "required": custom_errors["required"].format(field_name="Description"),
            "invalid": custom_errors["invalid_length"].format(field_name="Description")
        }
    )
    started_at = fields.DateTime(
        required=True,
        error_messages={
            "required": custom_errors["required"].format(field_name="Start date")
        }
    )
    completed_at = fields.DateTime(allow_none=True)
    hours_spent = fields.Float(allow_none=True)
    materials_cost = fields.Float(allow_none=True)
    materials = fields.List(fields.Str(), default=[])
    metals = fields.List(fields.Str(), default=[])
    gemstones = fields.List(fields.Str(), default=[])
    shape = fields.Str(allow_none=True)
    jewelry_type = fields.Str(allow_none=True)
