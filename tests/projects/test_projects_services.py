from bson import ObjectId

# Service functions
from application.modules.accounts.services import service_create_account
from application.modules.projects.services import (
    service_create_project, 
    service_get_project, 
    service_update_project, 
    service_delete_project
)

# Database utilities
from application.utils.database import pymongo


def test_service_create_project(app, base_account_data, base_project_data):
    with app.app_context():
        # Create the account
        accountId = service_create_account(base_account_data)
        assert accountId

        # Create the project with the associated accountId
        base_project_data["accountId"] = str(accountId)
        new_project = service_create_project(base_project_data, str(accountId))
        assert new_project

        # Assert that the new_project contains all the fields from the base_project_data
        for key, value in base_project_data.items():
            assert new_project.get(key) == value

        # Assert the projectId field is present and matches the MongoDB _id
        assert new_project.get("projectId") == str(new_project.get("_id"))

        # Assert the accountId field is present and matches the accountId used for creation
        assert new_project.get("accountId") == str(accountId)

    


def test_service_get_project(app, base_account_data, base_project_data):
    with app.app_context():
        accountId = service_create_account(base_account_data)
        projectId = service_create_project(base_project_data, str(accountId))

        project = service_get_project(str(projectId), str(accountId))
        
        assert project
        assert project["_id"] == projectId
        assert project["accountId"] == accountId


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

