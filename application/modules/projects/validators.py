from marshmallow import fields, Schema, ValidationError, validates_schema
from marshmallow.validate import Length
from application.utils.helpers import validate_not_empty_or_whitespace


class ProjectSchema(Schema):
    # Using ObjectId which is a hex string.
    account_id = fields.String(
        required=True,
        error_messages={
            "required": "Account ID is required."
        }
    )
    
    project_id = fields.String(dump_only=True)
    
    project_name = fields.Str(
        required=True,
        validate=validate_not_empty_or_whitespace,
        error_messages={
            "required": "Project name is required."
        }
    )
    
    description = fields.Str(
        required=True,
        validate=[
            Length(max=300, error="Description exceeds the maximum length."),
            validate_not_empty_or_whitespace
        ],
        error_messages={
            "required": "Description is required."
        }
    )
    
    started_at = fields.Date(
        required=True,
        error_messages={
            "required": "Start date is required."
        }
    )
    
    completed_at = fields.Date(allow_none=True)
    hours_spent = fields.Float(allow_none=True)
    materials_cost = fields.Float(allow_none=True)

    # 'dump_default' is used to specify a default value during the serialization (dumping) process.
    # 'load_default' is used to specify a default value during the deserialization (loading) process.
    materials = fields.List(fields.Str(), dump_default=[], load_default=[])
    metals = fields.List(fields.Str(), dump_default=[], load_default=[])
    gemstones = fields.List(fields.Str(), dump_default=[], load_default=[])   
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


@validates_schema
def validate_dates(self, data, **kwargs):
    if data.get('completed_at') and data.get('started_at') > data.get('completed_at'):
        raise ValidationError("Completion date cannot be before the start date.", "completed_at")