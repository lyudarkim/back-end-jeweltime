from flask import json


def test_create_account_route(app, base_account_data):
    with app.test_client() as client:
        response = client.post('/accounts', json=base_account_data)

        assert response.status_code == 201

        # Convert raw data into a Python dictionary
        json_data = json.loads(response.data)
        
        assert 'accountId' in json_data
        assert json_data["firstName"] == base_account_data["firstName"]
        assert json_data["lastName"] == base_account_data["lastName"]
        assert json_data["email"] == base_account_data["email"]
        assert json_data["zipcode"] == base_account_data["zipcode"]


def test_get_account_route(app, base_account_data):
    with app.test_client() as client:
        # Create an account to retrieve
        response = client.post('/accounts', json=base_account_data)

        # Parse JSON string to a Python dict to get 'accountId'
        accountId = json.loads(response.data)['accountId']

        response = client.get(f'/accounts/{accountId}')
        assert response.status_code == 200

        json_data = json.loads(response.data)

        assert json_data['accountId'] == accountId
        assert json_data["firstName"] == base_account_data["firstName"]
        assert json_data["lastName"] == base_account_data["lastName"]
        assert json_data["email"] == base_account_data["email"]
        assert json_data["zipcode"] == base_account_data["zipcode"]


def test_update_account_route(app, base_account_data):
    with app.test_client() as client:
        response = client.post('/accounts', json=base_account_data)
        accountId = json.loads(response.data)['accountId']

        update_data = {"firstName": "Lulu"}
        response = client.put(f'/accounts/{accountId}', json=update_data)
        assert response.status_code == 200
        
        json_data = json.loads(response.data)
        assert json_data["message"] == "Account updated successfully"


def test_delete_account_route(app, base_account_data):
    with app.test_client() as client:
        # Setting up an account to delete
        response = client.post('/accounts', json=base_account_data)
        accountId = json.loads(response.data)['accountId']

        # Testing DELETE on a specific account
        response = client.delete(f'/accounts/{accountId}')
        assert response.status_code == 200
        json_data = json.loads(response.data)
        assert json_data["message"] == "Account deleted successfully"

        # Confirm account is deleted by trying to get it
        response = client.get(f'/accounts/{accountId}')
        assert response.status_code == 404


def test_delete_account_route_invalid_id(app):
    with app.test_client() as client:
        # Testing DELETE route with an invalid accountId
        response = client.delete('/accounts/invalid_id')
        assert response.status_code == 400
        
        json_data = json.loads(response.data)
        assert json_data["error"] == "Invalid account ID format"

