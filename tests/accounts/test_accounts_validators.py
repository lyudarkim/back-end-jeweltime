from application.modules.accounts.validators import validate_account


def test_valid_account_data(base_account_data):
    data = base_account_data.copy()
    errors = validate_account(data)

    assert errors is None


# Tests for firstName
def test_first_name_is_not_empty_string(base_account_data):     
    data = base_account_data.copy()
    data["firstName"] = ""
    
    errors = validate_account(data)
    assert errors['firstName'] == ["Field cannot be empty or consist solely of whitespace."]


def test_first_name_is_not_whitespace_only(base_account_data):     
    data = base_account_data.copy()
    data["firstName"] = "     "
    
    errors = validate_account(data)
    assert errors['firstName'] == ["Field cannot be empty or consist solely of whitespace."]


def test_first_name_field_is_required(base_account_data):
    data = base_account_data.copy()
    del data["firstName"]
    
    errors = validate_account(data)
    assert errors['firstName'] == ["First name is required."]


# Tests for lastName
def test_last_name_is_not_empty_string(base_account_data):     
    data = base_account_data.copy()
    data["lastName"] = ""
    
    errors = validate_account(data)
    assert errors['lastName'] == ["Field cannot be empty or consist solely of whitespace."]


def test_last_name_is_not_whitespace_only(base_account_data):     
    data = base_account_data.copy()
    data["lastName"] = "     "
    
    errors = validate_account(data)
    assert errors['lastName'] == ["Field cannot be empty or consist solely of whitespace."]


def test_last_name_field_is_required(base_account_data):
    data = base_account_data.copy()
    del data["lastName"]
    
    errors = validate_account(data)
    assert errors['lastName'] == ["Last name is required."]


# Tests for email
def test_email_is_not_empty_string(base_account_data):     
    data = base_account_data.copy()
    data["email"] = ""
    
    errors = validate_account(data)
    assert errors['email'] == ["Not a valid email address."]


def test_email_is_not_whitespace_only(base_account_data):     
    data = base_account_data.copy()
    data["email"] = "     "
    
    errors = validate_account(data)
    assert errors['email'] == ["Not a valid email address."]


def test_email_field_is_required(base_account_data):
    data = base_account_data.copy()
    del data["email"]
    
    errors = validate_account(data)
    assert errors['email'] == ["Email is required."]


def test_valid_email_format(base_account_data):
    data = base_account_data.copy()
    errors = validate_account(data)

    assert errors is None

# Tests for zipcode
def test_zipcode_is_not_empty_string(base_account_data):     
    data = base_account_data.copy()
    data["zipcode"] = ""
    
    errors = validate_account(data)
    assert "Field cannot be empty or consist solely of whitespace." in errors['zipcode']


def test_zipcode_is_not_whitespace_only(base_account_data):     
    data = base_account_data.copy()
    data["zipcode"] = "     "
    
    errors = validate_account(data)
    assert errors['zipcode'] == ["Field cannot be empty or consist solely of whitespace."]


def test_zipcode_field_is_required(base_account_data):
    data = base_account_data.copy()
    del data["zipcode"]
    
    errors = validate_account(data)
    assert errors['zipcode'] == ["Zipcode is required."]


def test_zipcode_does_not_exceed_max_length(base_account_data):
    data = base_account_data.copy()
    data["zipcode"] = "12345678901"
    
    errors = validate_account(data)
    assert errors['zipcode'] == ["Length must be between 3 and 10."]


def test_zipcode_reaches_minimum_length(base_account_data):
    data = base_account_data.copy()
    data["zipcode"] = "12"
    
    errors = validate_account(data)
    assert errors['zipcode'] == ["Length must be between 3 and 10."]


def test_zipcode_with_min_length(base_account_data):
    data = base_account_data.copy()
    data["zipcode"] = "AHA"
    errors = validate_account(data)

    assert errors is None


def test_zipcode_with_max_length(base_account_data):
    data = base_account_data.copy()
    data["zipcode"] = "1234567890"
    errors = validate_account(data)

    assert errors is None