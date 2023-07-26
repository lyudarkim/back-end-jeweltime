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


def test_project_name_field_is_required(base_project_data):
    data = base_project_data.copy()
    del data["project_name"]
    
    errors = validate_project(data)
    assert errors['project_name'] == ["Project name is required."]