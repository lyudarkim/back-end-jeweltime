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


def test_create_project(app, base_account_data, base_project_data):
    with app.app_context():
        account_id = service_create_account(base_account_data)
        assert account_id

        project_id = service_create_project(base_project_data, str(account_id))
        assert project_id
        
        retrieved_project = pymongo.db.projects.find_one({"_id": project_id})
        assert retrieved_project["project_name"] == base_project_data["project_name"]
        assert retrieved_project["account_id"] == account_id


def test_get_project(app, base_account_data, base_project_data):
    with app.app_context():
        account_id = service_create_account(base_account_data)
        project_id = service_create_project(base_project_data, str(account_id))

        project = service_get_project(str(project_id), str(account_id))
        
        assert project
        assert project["_id"] == project_id
        assert project["account_id"] == account_id


def test_update_project(app, base_account_data, base_project_data):
    with app.app_context():
        account_id = service_create_account(base_account_data)
        project_id = service_create_project(base_project_data, str(account_id))

        updated_data = {"project_name": "New Project Name"}
        count = service_update_project(str(project_id), str(account_id), updated_data)

        assert count == 1
        
        project = pymongo.db.projects.find_one({"_id": project_id})
        assert project["project_name"] == "New Project Name"
        assert str(project["account_id"]) == str(account_id)


def test_delete_project(app, base_account_data, base_project_data):
    with app.app_context():
        account_id = service_create_account(base_account_data)
        project_id = service_create_project(base_project_data, str(account_id))

        count = service_delete_project(str(project_id), str(account_id))
        assert count == 1
        
        project = pymongo.db.projects.find_one({"_id": project_id})
        assert not project

