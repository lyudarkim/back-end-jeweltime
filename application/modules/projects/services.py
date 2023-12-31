from bson.objectid import ObjectId
from application.utils.database import pymongo
from application.utils.exceptions import AccountNotFoundException, ProjectNotFoundException


def service_create_project(data):
    """This function inserts a new project into the database and associates it with an account."""

    accountId = data["accountId"]

    if not pymongo.db.accounts.find_one({"accountId": accountId}):
        raise AccountNotFoundException()
    
    # Insert the new project and get the _id generated by MongoDB
    inserted = pymongo.db.projects.insert_one(data)
    projectId = inserted.inserted_id

    # Check if insertion was acknowledged by db
    if not inserted.acknowledged:
        raise Exception("Failed to add project into the database")
    
    # Update newly inserted project to set projectId which will be the same value as _id
    pymongo.db.projects.update_one({"_id": projectId}, {"$set": {"projectId": str(projectId)}})

    # Fetch the newly created project
    new_project = pymongo.db.projects.find_one({"_id": ObjectId(projectId)})

    # Remove the non-serializable BSON ObjectId from the dictionary before returning the POST response body
    del new_project["_id"]

    return new_project

    
def service_get_project(projectId):
    """This function retrieves a project using the project ID."""

    project = pymongo.db.projects.find_one({"_id": ObjectId(projectId)})

    if not project:
        raise ProjectNotFoundException()
    
    # Delete the '_id' key-value pair because we don't want it in GET response body
    del project["_id"]

    return project


def service_get_all_projects(accountId):
    """This function retrieves all projects associated with an account using the account ID."""

    # Check if the account ID exists in the 'accounts' collection of the db
    if not pymongo.db.accounts.find_one({"accountId": accountId}):
        raise AccountNotFoundException()

    # Retrieve all projects from the 'projects' collection that are associated with the account ID
    projects = pymongo.db.projects.find({"accountId": accountId})

    all_projects = [project for project in projects]
    
    for project in all_projects:
        project.pop("_id")

    return all_projects


def service_update_project(projectId, data):
    """This function updates a project using the project ID and returns the updated project object."""

    result = pymongo.db.projects.update_one(
        {"projectId": projectId},
        {"$set": data}
    )

    # Check if a project with the given projectId exists
    if result.matched_count == 0:
        raise ProjectNotFoundException()
    
    # Fetch the updated project
    updated_project = pymongo.db.projects.find_one({"projectId": projectId})
    del updated_project["_id"]
    
    return updated_project


def service_delete_project(projectId):
    """
    This function deletes a project using the project ID.
    It raises a ProjectNotFoundException if the project does not exist.
    """
    # Delete the project
    result = pymongo.db.projects.delete_one({"_id": ObjectId(projectId)})
    
    # If the project was not found, raise an exception
    if result.deleted_count == 0:
        raise ProjectNotFoundException()

    