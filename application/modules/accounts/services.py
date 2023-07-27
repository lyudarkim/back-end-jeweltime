from application.utils.database import pymongo


def create_account(data):
    """Insert new account into the database."""
    return pymongo.db.accounts.insert_one(data).inserted_id

