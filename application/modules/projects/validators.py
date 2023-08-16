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

    materials = fields.Str(
        required=True,
        validate=[
            Length(max=300, error="Materials exceed the maximum length."),
            validate_not_empty_or_whitespace
        ],
        error_messages={
            "required": "Materials are required."
        }
    )

    startedAt = fields.Date(
        required=True,
        error_messages={
            "required": "Start date is required."
        }
    )

    completedAt = fields.Str(allow_none=True)
    hoursSpent = fields.Str(allow_none=True)
    materialsCost = fields.Str(allow_none=True)
    metals = fields.Str(allow_none=True)
    gemstones = fields.Str(allow_none=True)
    notes = fields.Str(allow_none=True) 
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

