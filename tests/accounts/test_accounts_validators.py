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


def test_first_name_is_not_whitespace_only():     
    schema = AccountSchema()
    data = {
        "first_name": "     ",  
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


def test_last_name_is_not_whitespace_only():     
    schema = AccountSchema()
    data = {
        "first_name": "Juniper",
        "last_name": "     ",  
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


# Tests for email
def test_email_is_not_empty_string():     
    schema = AccountSchema()
    data = {
        "first_name": "Juniper",
        "last_name": "Didion",
        "email": "",   
        "zipcode": "98104"
    }
    
    with pytest.raises(ValidationError) as excinfo:
        schema.load(data)

    assert excinfo.value.messages['email'] == ["Not a valid email address."]


def test_email_is_not_whitespace_only():     
    schema = AccountSchema()
    data = {
        "first_name": "Juniper",
        "last_name": "Didion",
        "email": "     ",  
        "zipcode": "98104"
    }
    
    with pytest.raises(ValidationError) as excinfo:
        schema.load(data)

    # Whitespace only for email will still trigger "Not a valid email address."
    assert excinfo.value.messages['email'] == ["Not a valid email address."]


def test_email_field_is_required():
    schema = AccountSchema()
    data = {
        "first_name": "Juniper",
        "last_name": "Didion",
        "zipcode": "98104"
    }
    
    with pytest.raises(ValidationError) as excinfo:
        schema.load(data)

    assert excinfo.value.messages['email'] == ["Email is required."]


# Tests for zipcode
def test_zipcode_is_not_empty_string():     
    schema = AccountSchema()
    data = {
        "first_name": "Juniper",
        "last_name": "Didion",
        "email": "juniper@didion.com",
        "zipcode": ""  
    }
    
    with pytest.raises(ValidationError) as excinfo:
        schema.load(data)

    assert "Field cannot be empty or consist solely of whitespace." in excinfo.value.messages['zipcode']


def test_zipcode_is_not_whitespace_only():     
    schema = AccountSchema()
    data = {
        "first_name": "Juniper",
        "last_name": "Didion",
        "email": "juniper@didion.com",
        "zipcode": "     "  
    }
    
    with pytest.raises(ValidationError) as excinfo:
        schema.load(data)

    assert excinfo.value.messages['zipcode'] == ["Field cannot be empty or consist solely of whitespace."]


def test_zipcode_field_is_required():
    schema = AccountSchema()
    data = {
        "first_name": "Juniper",
        "last_name": "Didion",
        "email": "juniper@didion.com",
    }
    
    with pytest.raises(ValidationError) as excinfo:
        schema.load(data)

    assert excinfo.value.messages['zipcode'] == ["Zipcode is required."]


def test_zipcode_does_not_exceed_max_length():
    schema = AccountSchema()
    data = {
        "first_name": "Juniper",
        "last_name": "Didion",
        "email": "juniper@didion.com",
        "zipcode": "12345678901"  
    }
    
    with pytest.raises(ValidationError) as excinfo:
        schema.load(data)

    assert excinfo.value.messages['zipcode'] == ["Length must be between 3 and 10."]


def test_zipcode_reaches_minimum_length():
    schema = AccountSchema()
    data = {
        "first_name": "Juniper",
        "last_name": "Didion",
        "email": "juniper@didion.com",
        "zipcode": "12"  
    }
    
    with pytest.raises(ValidationError) as excinfo:
        schema.load(data)

    assert excinfo.value.messages['zipcode'] == ["Length must be between 3 and 10."]
