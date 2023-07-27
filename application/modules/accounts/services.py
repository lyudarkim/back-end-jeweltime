from bson import ObjectId
from application.utils.database import pymongo


def create_account(data):
    """This function inserts a new account into the database."""
    return pymongo.db.accounts.insert_one(data).inserted_id


def get_account(account_id):
    """This function retrieves a specific account using its ID."""
    return pymongo.db.accounts.find_one({"_id": ObjectId(account_id)})


def update_account(account_id, data):
    """
    This function updates an account in the database using its ID. 
    It returns the count of updated records (should be 1 if the operation was successful).
    """
    result = pymongo.db.accounts.update_one({"_id": ObjectId(account_id)}, {"$set": data})
    
    return result.modified_count
    