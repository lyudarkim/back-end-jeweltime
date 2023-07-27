from bson import ObjectId
from application.utils.database import pymongo


def create_account(data):
    """Insert new account into the database."""
    return pymongo.db.accounts.insert_one(data).inserted_id


def get_account(account_id):
    """Get a specific account using its ID."""
    return pymongo.db.accounts.find_one({"_id": ObjectId(account_id)})
