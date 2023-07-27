from application.modules.accounts.services import create_account, get_account, update_account, delete_account
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


def test_update_account(app, base_account_data):
    with app.app_context():
        account_id = create_account(base_account_data)
        updated_data = {"first_name": "Lulu"}

        count = update_account(str(account_id), updated_data)
        assert count == 1
        
        account = pymongo.db.accounts.find_one({"_id": account_id})
        assert account["first_name"] == "Lulu"


def test_delete_account(app, base_account_data):
    with app.app_context():
        account_id = create_account(base_account_data)
        count = delete_account(str(account_id))
        assert count == 1
        
        account = pymongo.db.accounts.find_one({"_id": account_id})
        assert not account