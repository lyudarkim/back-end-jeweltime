from marshmallow import ValidationError


def validate_not_only_whitespace(data):
    """Ensure the provided data isn't just whitespace."""
    if data.strip() == "":
        raise ValidationError("Field cannot consist solely of whitespace.")
