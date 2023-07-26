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


# Tests for started_at
def test_started_at_is_required(base_project_data):
    data = base_project_data.copy()
    del data["started_at"]
    
    errors = validate_project(data)
    assert errors['started_at'] == ["Start date is required."]


# Tests for completed_at (optional field)
def test_valid_project_data_with_completed_at(base_project_data):
    data = base_project_data.copy()

    # Remove 'project_id' from the data
    data.pop("project_id", None)   
    validated_data = validate_project(data)

    assert "project_name" in validated_data
    assert "description" in validated_data
    assert "started_at" in validated_data
    assert "completed_at" in validated_data

    # Format the date before comparison
    validated_started_at = validated_data["started_at"].strftime('%Y-%m-%d')
    assert validated_started_at == data["started_at"]


# Tests for date validation
def test_start_date_is_not_after_completion_date(invalid_project_data):
    data = invalid_project_data.copy()

    errors = validate_project(data)
    assert errors['completed_at'] == ["Completion date cannot be before the start date."]