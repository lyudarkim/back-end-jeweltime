import pytest
from marshmallow import ValidationError
from application.modules.accounts.validators import AccountSchema


# Tests for first_name
def test_first_name_is_not_empty_string():     
    schema = AccountSchema()
    data = {
        "first_name": "",  
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
        "last_name": "Didion",
        "email": "juniper@didion.com",
        "zipcode": "98104"
    }
    
    with pytest.raises(ValidationError) as excinfo:
        schema.load(data)

    assert excinfo.value.messages['first_name'] == ["First name is required."]


# Tests for last_name
def test_last_name_is_not_empty_string():     
    schema = AccountSchema()
    data = {
        "first_name": "Juniper",
        "last_name": "",  
        "email": "juniper@didion.com",
        "zipcode": "98104"
    }
    
    with pytest.raises(ValidationError) as excinfo:
        schema.load(data)

    assert excinfo.value.messages['last_name'] == ["Field cannot be empty or consist solely of whitespace."]


def test_last_name_field_is_required():
    schema = AccountSchema()
    data = {
        "first_name": "Juniper",
        "email": "juniper@didion.com",
        "zipcode": "98104"
    }
    
    with pytest.raises(ValidationError) as excinfo:
        schema.load(data)

    assert excinfo.value.messages['last_name'] == ["Last name is required."]
