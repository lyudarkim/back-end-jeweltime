# Service functions
from application.modules.projects.services import (
    service_create_project, 
    service_get_project, 
    # service_update_project, 
    # service_delete_project
)

# Database utilities
from application.utils.database import pymongo


def test_create_project(app, base_project_data):
    with app.app_context():
        project_id = service_create_project(base_project_data)
        assert project_id
        
        retrieved_project = pymongo.db.projects.find_one({"_id": project_id})
        assert retrieved_project["project_name"] == base_project_data["project_name"]


def test_get_project(app, base_project_data):
    with app.app_context():
        project_id = service_create_project(base_project_data)
        project = service_get_project(str(project_id))
        
        assert project
        assert project["_id"] == project_id