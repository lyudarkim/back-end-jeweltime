from bson import ObjectId
from application.utils.database import pymongo


def service_create_project(data, account_id):
    """This function inserts a new project into the database and associates it with an account."""
    
    if not pymongo.db.accounts.find_one({"_id": ObjectId(account_id)}):
        raise ValueError("Account not found.")
    
    # Add key-value pair with the account_id to the project
    data["account_id"] = ObjectId(account_id)  

    return pymongo.db.projects.insert_one(data).inserted_id

    
def service_get_project(project_id, account_id):
    """This function retrieves a project associated with an account using project ID and account ID."""

    if not pymongo.db.accounts.find_one({"_id": ObjectId(account_id)}):
        raise ValueError("Account not found.")

    return pymongo.db.projects.find_one({"_id": ObjectId(project_id)})


def service_update_project(project_id, account_id, data):
    """This function updates a project associated with an account using project ID and account ID."""

    if not pymongo.db.accounts.find_one({"_id": ObjectId(account_id)}):
        raise ValueError("Account not found.")

    result = pymongo.db.projects.update_one(
        {"_id": ObjectId(project_id), "account_id": ObjectId(account_id)},
        {"$set": data}
    )
    return result.modified_count
    