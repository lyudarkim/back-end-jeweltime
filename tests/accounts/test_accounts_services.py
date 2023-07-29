# Service functions
from application.modules.accounts.services import (
    service_create_account, 
    service_get_account, 
    service_update_account, 
    service_delete_account
)

# Database utilities
from application.utils.database import pymongo


def test_service_create_account(app, base_account_data):
    with app.app_context():
        new_account = service_create_account(base_account_data)
        
        assert new_account is not None, "Account not created"
        assert 'account_id' in new_account
        assert str(new_account['_id']) == new_account['account_id']
        assert new_account["first_name"] == base_account_data["first_name"]
        assert new_account["last_name"] == base_account_data["last_name"]
        assert new_account["email"] == base_account_data["email"]
        assert new_account["zipcode"] == base_account_data["zipcode"]


def test_service_get_account(app, base_account_data):
    with app.app_context():
        account_id = service_create_account(base_account_data)
        account = service_get_account(str(account_id))
        
        assert account
        assert account["_id"] == account_id


def test_service_update_account(app, base_account_data):
    with app.app_context():
        account_id = service_create_account(base_account_data)
        updated_data = {"first_name": "Lulu"}

        count = service_update_account(str(account_id), updated_data)
        assert count == 1
        
        account = pymongo.db.accounts.find_one({"_id": account_id})
        assert account["first_name"] == "Lulu"


def test_service_delete_account(app, base_account_data):
    with app.app_context():
        account_id = service_create_account(base_account_data)
        count = service_delete_account(str(account_id))
        assert count == 1
        
        account = pymongo.db.accounts.find_one({"_id": account_id})
        assert not account