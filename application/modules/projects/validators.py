from marshmallow import Schema, Length, fields


class ProjectSchema(Schema):

    project_id = fields.Integer(dump_only=True)
    project_name = fields.Str(required=True)
    description = fields.Str(required=True, validate=Length(max=250))
    started_at = fields.DateTime(required=True)
    completed_at = fields.DateTime(allow_none=True)
    hours_spent = fields.Float(allow_none=True)
    materials_cost = fields.Float(allow_none=True)
    materials = fields.List(fields.Str(), default=[])
    metals = fields.List(fields.Str(), default=[])
    gemstones = fields.List(fields.Str(), default=[])
    shape = fields.Str(allow_none=True)
    jewelry_type = fields.Str(allow_none=True)
    account_id = fields.Integer(required=True)
