from bson import ObjectId
from application.utils.database import pymongo
from application.utils.exceptions import AccountNotFoundException


def service_create_account(data):
    """This function inserts an account into the database with the accountId and returns the account object."""

    # Insert new account. MongoDB will generate an _id
    inserted = pymongo.db.accounts.insert_one(data)
    accountId = inserted.inserted_id

    # Check if insertion was acknowledged by db
    if not inserted.acknowledged:
        raise Exception("Failed to add account into the database")
    
    # Update newly inserted account to set accountId which will be the same value as _id
    pymongo.db.accounts.update_one({"_id": accountId}, {"$set": {"accountId": str(accountId)}})

    # Fetch the updated account
    new_account = pymongo.db.accounts.find_one({"_id": ObjectId(accountId)})
    
    # Remove the non-serializable BSON ObjectId from the dictionary before returning the POST response body
    del new_account["_id"]

    return new_account


def service_get_account(accountId):
    """This function retrieves a specific account using its account ID."""

    account = pymongo.db.accounts.find_one({"accountId": accountId})

    if not account:
        raise AccountNotFoundException()
    
    # Delete the '_id' key-value pair because we don't want it in GET response body
    del account["_id"]  

    return account 


def service_update_account(accountId, data):
    """
    This function updates an account in the database using its account ID and returns the updated account object.
    """

    result = pymongo.db.accounts.update_one({"accountId": accountId}, {"$set": data})
    
    if result.modified_count == 0:
        raise AccountNotFoundException()

    # Fetch the updated account
    updated_account = pymongo.db.accounts.find_one({"accountId": accountId})
    
    del updated_account["_id"]
    
    return updated_account
    

def service_delete_account(accountId):
    """
    This function deletes an account and all the projects associated with that account from the database using the account ID.
    It returns the count of deleted account records (should be 1 if the operation was successful).
    """

    account_deletion_result = pymongo.db.accounts.delete_one({"accountId": accountId})
    
    if account_deletion_result.deleted_count == 0:
        return None
    
    # Now delete the projects associated with this account
    projects_deletion_result = pymongo.db.projects.delete_many({"accountId": accountId})

    if projects_deletion_result.deleted_count == 0:
        return None
    
    return account_deletion_result.deleted_count
