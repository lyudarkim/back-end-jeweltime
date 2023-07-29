from bson import ObjectId
from application.utils.database import pymongo


def service_create_account(account_data):
    """This function inserts an account into the database with the account_id and returns the account object."""

    # Insert new account. MongoDB will generate an _id.
    inserted = pymongo.db.accounts.insert_one(account_data)
    account_id = inserted.inserted_id

    # Check if insertion was acknowledged by db.
    if not inserted.acknowledged:
        raise Exception("Failed to insert account into the database")
    
    # Update newly inserted account to set account_id which will be the same value as _id.
    pymongo.db.accounts.update_one({"_id": account_id}, {"$set": {"account_id": str(account_id)}})

    # Fetch the updated account.
    new_account = pymongo.db.accounts.find_one({"_id": ObjectId(account_id)})
    
    # Remove the non-serializable BSON ObjectId from the dictionary before returning.
    del new_account["_id"]

    return new_account


def service_get_account(account_id):
    """This function retrieves a specific account using its ID."""
    return pymongo.db.accounts.find_one({"_id": ObjectId(account_id)})  


def service_update_account(account_id, data):
    """
    This function updates an account in the database using its ID. 
    It returns the count of updated records (should be 1 if the operation was successful).
    """
    result = pymongo.db.accounts.update_one({"_id": ObjectId(account_id)}, {"$set": data})
    
    return result.modified_count
    

def service_delete_account(account_id):
    """
    This function deletes an account from the database using its ID.
    It returns the count of deleted records (should be 1 if the operation was successful).
    """
    result = pymongo.db.accounts.delete_one({"_id": ObjectId(account_id)})

    return result.deleted_count
