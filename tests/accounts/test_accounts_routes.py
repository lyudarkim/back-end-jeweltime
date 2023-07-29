from flask import json


def test_create_account_route(app, base_account_data):
    with app.test_client() as client:
        response = client.post('/accounts', json=base_account_data)

        assert response.status_code == 201

        # Convert raw data into a Python dictionary
        json_data = json.loads(response.data)
        
        assert 'account_id' in json_data
        assert json_data['account_id'] == str(json_data['_id'])
        assert json_data["first_name"] == base_account_data["first_name"]
        assert json_data["last_name"] == base_account_data["last_name"]
        assert json_data["email"] == base_account_data["email"]
        assert json_data["zipcode"] == base_account_data["zipcode"]


def test_get_account_route(app, base_account_data):
    with app.test_client() as client:
        # Create an account to retrieve
        response = client.post('/accounts', json=base_account_data)

        # Parse JSON string to a Python dict to get 'account_id
        account_id = json.loads(response.data)['account_id']

        response = client.get(f'/accounts/{account_id}')
        assert response.status_code == 200

        json_data = json.loads(response.data)

        assert json_data['account_id'] == account_id
        assert json_data["first_name"] == base_account_data["first_name"]
        assert json_data["last_name"] == base_account_data["last_name"]
        assert json_data["email"] == base_account_data["email"]
        assert json_data["zipcode"] == base_account_data["zipcode"]


def test_update_account_route(app, base_account_data):
    with app.test_client() as client:
        response = client.post('/accounts', json=base_account_data)
        account_id = json.loads(response.data)['account_id']

        update_data = {"first_name": "Lulu"}
        response = client.put(f'/accounts/{account_id}', json=update_data)
        assert response.status_code == 200
        
        json_data = json.loads(response.data)
        assert json_data["message"] == "Account updated successfully"


def test_delete_account_route(app, base_account_data):
    with app.test_client() as client:
        # Setting up an account to delete
        response = client.post('/accounts', json=base_account_data)
        account_id = json.loads(response.data)['account_id']

        # Testing DELETE on a specific account
        response = client.delete(f'/accounts/{account_id}')
        assert response.status_code == 200
        json_data = json.loads(response.data)
        assert json_data["message"] == "Account deleted successfully"

        # Confirm account is deleted by trying to get it
        response = client.get(f'/accounts/{account_id}')
        assert response.status_code == 404


def test_delete_account_route_invalid_id(app):
    with app.test_client() as client:
        # Testing DELETE route with an invalid account_id
        response = client.delete('/accounts/invalid_id')
        assert response.status_code == 400
        
        json_data = json.loads(response.data)
        assert json_data["error"] == "Invalid account ID format"

