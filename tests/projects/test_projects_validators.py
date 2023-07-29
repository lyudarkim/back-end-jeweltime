from application.modules.projects.validators import validate_project


# Tests for projectName
def test_project_name_is_not_empty_string(base_project_data):
    data = base_project_data.copy()
    data["projectName"] = ""
    
    errors = validate_project(data)
    assert errors['projectName'] == ["Field cannot be empty or consist solely of whitespace."]


def test_project_name_is_not_whitespace_only(base_project_data):
    data = base_project_data.copy()
    data["projectName"] = "     "
    
    errors = validate_project(data)
    assert errors['projectName'] == ["Field cannot be empty or consist solely of whitespace."]


def test_project_name_is_required(base_project_data):
    data = base_project_data.copy()
    del data["projectName"]
    
    errors = validate_project(data)
    assert errors['projectName'] == ["Project name is required."]


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


# Tests for accountId
def test_account_id_is_required(base_project_data):
    data = base_project_data.copy()
    del data["accountId"]
    
    errors = validate_project(data)
    assert errors['accountId'] == ["Account ID is required."]


# Tests for startedAt
def test_started_at_is_required(base_project_data):
    data = base_project_data.copy()
    del data["startedAt"]
    
    errors = validate_project(data)
    assert errors['startedAt'] == ["Start date is required."]


# Tests for completedAt (optional field)
def test_valid_project_data_with_completed_at(base_project_data):
    data = base_project_data.copy()

    # Remove 'projectId' from the data
    data.pop("projectId", None)   
    validated_data = validate_project(data)

    assert validated_data is None


# Tests for date validation
def test_start_date_is_not_after_completion_date(invalid_project_data):
    data = invalid_project_data.copy()

    errors = validate_project(data)
    assert errors['completedAt'] == ["Completion date cannot be before the start date."]