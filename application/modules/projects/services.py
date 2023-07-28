from bson import ObjectId
from application.utils.database import pymongo


def service_create_project(data):
    """This function inserts a new project into the database."""
    return pymongo.db.projects.insert_one(data).inserted_id
    

def service_get_project(project_id):
    """This function retrieves a specific project using its ID."""
    return pymongo.db.projects.find_one({"_id": ObjectId(project_id)})
    