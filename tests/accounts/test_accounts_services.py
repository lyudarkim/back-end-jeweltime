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
        assert 'accountId' in new_account
        assert new_account["firstName"] == base_account_data["firstName"]
        assert new_account["lastName"] == base_account_data["lastName"]
        assert new_account["email"] == base_account_data["email"]
        assert new_account["zipcode"] == base_account_data["zipcode"]


def test_service_get_account(app, base_account_data):
    with app.app_context():
        created_account = service_create_account(base_account_data)
        accountId = created_account['accountId']
        retrieved_account = service_get_account(accountId)
        
        assert retrieved_account
        assert retrieved_account['accountId'] == accountId
        assert retrieved_account["firstName"] == base_account_data["firstName"]
        assert retrieved_account["lastName"] == base_account_data["lastName"]
        assert retrieved_account["email"] == base_account_data["email"]
        assert retrieved_account["zipcode"] == base_account_data["zipcode"]


def test_service_update_account(app, base_account_data):
    with app.app_context():
        accountId = service_create_account(base_account_data)
        updated_data = {"firstName": "Lulu"}

        count = service_update_account(str(accountId), updated_data)
        assert count == 1
        
        account = pymongo.db.accounts.find_one({"_id": accountId})
        assert account["firstName"] == "Lulu"


def test_service_delete_account(app, base_account_data):
    with app.app_context():
        accountId = service_create_account(base_account_data)
        count = service_delete_account(str(accountId))
        assert count == 1
        
        account = pymongo.db.accounts.find_one({"_id": accountId})
        assert not account