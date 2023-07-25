from marshmallow import fields, Schema, ValidationError
from marshmallow.validate import Length
from application.utils.helpers import validate_not_only_whitespace


class ProjectSchema(Schema):
    # Using ObjectId which is a hex string.
    account_id = fields.String(
        required=True,
        error_messages={"required": "Account ID is required."}
    )
    
    project_id = fields.String(dump_only=True)
    
    project_name = fields.Str(
        required=True,
        validate=[
            Length(min=1, error="Field cannot be empty."),
            validate_not_only_whitespace
        ],
        error_messages={"required": "Project name is required."}
    )
    
    description = fields.Str(
        required=True,
        validate=[
            Length(max=300, error="Description exceeds the maximum length."),
            validate_not_only_whitespace
        ],
        error_messages={"required": "Description is required."}
    )
    
    started_at = fields.DateTime(
        required=True,
        error_messages={"required": "Start date is required."}
    )
    
    completed_at = fields.DateTime(allow_none=True)
    hours_spent = fields.Float(allow_none=True)
    materials_cost = fields.Float(allow_none=True)
    materials = fields.List(fields.Str(), default=[])
    metals = fields.List(fields.Str(), default=[])
    gemstones = fields.List(fields.Str(), default=[])
    shape = fields.Str(allow_none=True)
    jewelry_type = fields.Str(allow_none=True)


def validate_project(data):
    """Validates project data against the ProjectSchema."""
    schema = ProjectSchema()
    try:
        validated_data = schema.load(data)
        return validated_data
    except ValidationError as error:
        return error.messages
