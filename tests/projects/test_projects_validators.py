from application.modules.projects.validators import validate_project


# Tests for project_name
def test_project_name_is_not_empty_string(base_project_data):
    data = base_project_data.copy()
    data["project_name"] = ""
    
    errors = validate_project(data)
    assert errors['project_name'] == ["Field cannot be empty or consist solely of whitespace."]


def test_project_name_is_not_whitespace_only(base_project_data):
    data = base_project_data.copy()
    data["project_name"] = "     "
    
    errors = validate_project(data)
    assert errors['project_name'] == ["Field cannot be empty or consist solely of whitespace."]


def test_project_name_is_required(base_project_data):
    data = base_project_data.copy()
    del data["project_name"]
    
    errors = validate_project(data)
    assert errors['project_name'] == ["Project name is required."]


# Tests for description
def test_description_is_not_empty_string(base_project_data):
    data = base_project_data.copy()
    data["description"] = ""
    
    errors = validate_project(data)
    assert errors['description'] == ["Field cannot be empty or consist solely of whitespace."]


def test_description_is_not_whitespace_only(base_project_data):
    data = base_project_data.copy()
    data["description"] = "     "
    
    errors = validate_project(data)
    assert errors['description'] == ["Field cannot be empty or consist solely of whitespace."]


def test_description_is_required(base_project_data):
    data = base_project_data.copy()
    del data["description"]
    
    errors = validate_project(data)
    assert errors['description'] == ["Description is required."]


def test_description_does_not_exceed_max_length(base_project_data):
    data = base_project_data.copy()
    data["description"] = "a" * 301  # One character more than the maximum
    
    errors = validate_project(data)
    assert errors["description"] == ["Description exceeds the maximum length."]


# Tests for account_id
def test_account_id_is_required(base_project_data):
    data = base_project_data.copy()
    del data["account_id"]
    
    errors = validate_project(data)
    assert errors['account_id'] == ["Account ID is required."]