from marshmallow import fields, Schema, ValidationError, validates_schema
from marshmallow.validate import Length
from application.utils.helpers import validate_not_empty_or_whitespace


class ProjectSchema(Schema):
    # Using ObjectId which is a hex string.
    accountId = fields.Str(
        required=True,
        validate=validate_not_empty_or_whitespace,
        error_messages={
            "required": "Account ID is required."
        }
    )


    projectId = fields.Str(dump_only=True)
    projectName = fields.Str(
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

    startedAt = fields.Date(
        required=True,
        error_messages={
            "required": "Start date is required."
        }
    )

    completedAt = fields.Date(allow_none=True)
    hoursSpent = fields.Float(allow_none=True)
    materialsCost = fields.Float(allow_none=True)

    # 'dump_default' is used to specify a default value during the serialization (dumping) process.
    # 'load_default' is used to specify a default value during the deserialization (loading) process.
    materials = fields.List(fields.Str(), dump_default=[], load_default=[])
    metals = fields.List(fields.Str(), dump_default=[], load_default=[])
    gemstones = fields.List(fields.Str(), dump_default=[], load_default=[])   
    notes = fields.List(fields.Str(), dump_default=[], load_default=[])   
    shape = fields.Str(allow_none=True)
    jewelryType = fields.Str(allow_none=True)

    @validates_schema
    def validate_dates(self, data, **kwargs):
        if data.get('completedAt') and data.get('startedAt') > data.get('completedAt'):
            raise ValidationError(
                "Completion date cannot be before the start date.",
                "completedAt"
            )
        

def validate_project(data, partial=False):
    """Validates project data against the ProjectSchema."""
    schema = ProjectSchema()
    schema.load(data, partial=partial)

