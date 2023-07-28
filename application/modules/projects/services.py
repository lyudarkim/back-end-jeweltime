from bson import ObjectId
from application.utils.database import pymongo


def service_create_project(data):
    """This function inserts a new project into the database."""
    return pymongo.db.projects.insert_one(data).inserted_id
    


    