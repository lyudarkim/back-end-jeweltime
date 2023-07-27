from application.modules.accounts.services import create_account, get_account
from application.utils.database import pymongo


def test_create_account(app, base_account_data):
    with app.app_context():
        account_id = create_account(base_account_data)
        assert account_id
        
        retrieved_account = pymongo.db.accounts.find_one({"_id": account_id})
        assert retrieved_account["first_name"] == base_account_data["first_name"]


def test_get_account(app, base_account_data):
    with app.app_context():
        account_id = create_account(base_account_data)
        account = get_account(str(account_id))
        
        assert account
        assert account["_id"] == account_id