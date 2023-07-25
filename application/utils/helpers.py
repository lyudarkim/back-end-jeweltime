from marshmallow import ValidationError


def validate_not_empty_or_whitespace(data):
    """Ensure the provided data isn't just whitespace or empty."""
    if not data or data.strip() == "":
        raise ValidationError("Field cannot be empty or consist solely of whitespace.")
