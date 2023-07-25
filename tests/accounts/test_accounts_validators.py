import pytest
from marshmallow import ValidationError
from application.modules.accounts.validators import AccountSchema


def test_first_name_is_not_empty_string():     
    schema = AccountSchema()
    data = {
        "first_name": "",   # Empty first_name
        "last_name": "Didion",
        "email": "juniper@didion.com",
        "zipcode": "98104"
    }
    
    with pytest.raises(ValidationError) as excinfo:
        schema.load(data)

    assert excinfo.value.messages['first_name'] == ["Field cannot be empty or consist solely of whitespace."]


def test_first_name_field_is_required():
    schema = AccountSchema()
    data = {
        # Omitting "first_name" to trigger the "required" validation
        "last_name": "Didion",
        "email": "juniper@didion.com",
        "zipcode": "98104"
    }
    
    with pytest.raises(ValidationError) as excinfo:
        schema.load(data)

    assert excinfo.value.messages['first_name'] == ["First name is required."]


