from bson import ObjectId

# Service functions
from application.modules.accounts.services import service_create_account
from application.modules.projects.services import (
    service_create_project, 
    service_get_project,
    service_get_all_projects, 
    service_update_project, 
    service_delete_project
)

# Database utilities
from application.utils.database import pymongo


def test_service_create_project(app, base_account_data, base_project_data):
    with app.app_context():
        # Create a new account
        account = service_create_account(base_account_data)
        assert account

        # Extract the accountId from the account object
        accountId = account["accountId"]

        # Create the project with the associated accountId
        base_project_data["accountId"] = accountId
        new_project = service_create_project(base_project_data, accountId)
        assert new_project

        # Check that the new_project contains all the fields from the base_project_data
        for key, value in base_project_data.items():
            if key == '_id':
                continue
            assert new_project.get(key) == value

        assert "projectId" in new_project

        # Verify the projectId field matches the expected string representation of the MongoDB ObjectId
        assert ObjectId(new_project.get("projectId"))  
        assert new_project.get("accountId") == accountId

    
def test_service_get_project(app, base_account_data, base_project_data):
    with app.app_context():
        account = service_create_account(base_account_data)
        accountId = account["accountId"]

        new_project = service_create_project(base_project_data, accountId)
        projectId = new_project["projectId"]

        project = service_get_project(projectId, accountId)
        
        assert project
        assert project["projectId"] == projectId


def test_service_get_all_projects(app, base_account_data, base_project_data):
    with app.app_context():
        account = service_create_account(base_account_data)
        assert account

        accountId = account["accountId"]
        base_project_data["accountId"] = accountId

        # If '_id' exists in base_project_data, remove it to avoid duplicates
        base_project_data.pop('_id', None)

        service_create_project(base_project_data.copy(), accountId)  
        service_create_project(base_project_data.copy(), accountId)

        # Retrieve all projects associated with the account
        retrieved_projects = service_get_all_projects(accountId)
        
        assert retrieved_projects is not None, "No projects retrieved"
        assert len(retrieved_projects) == 2, "Not all projects retrieved"
        
        for project in retrieved_projects:
            assert project["description"] == base_project_data["description"]


def test_service_update_project(app, base_account_data, base_project_data):
    with app.app_context():
        accountId = service_create_account(base_account_data)
        projectId = service_create_project(base_project_data, str(accountId))

        updated_data = {"projectName": "New Project Name"}
        count = service_update_project(str(projectId), str(accountId), updated_data)

        assert count == 1
        
        project = pymongo.db.projects.find_one({"_id": projectId})
        assert project["projectName"] == "New Project Name"
        assert str(project["accountId"]) == str(accountId)


def test_service_delete_project(app, base_account_data, base_project_data):
    with app.app_context():
        accountId = service_create_account(base_account_data)
        projectId = service_create_project(base_project_data, str(accountId))

        count = service_delete_project(str(projectId), str(accountId))
        assert count == 1
        
        project = pymongo.db.projects.find_one({"_id": projectId})
        assert not project

