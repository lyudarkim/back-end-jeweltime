from flask import json


def test_create_account(app, base_account_data):
    with app.test_client() as client:
        response = client.post('/accounts', json=base_account_data)

        assert response.status_code == 201

        # Convert raw data into a Python dictionary
        json_data = json.loads(response.data)
        account_id = json_data['account_id']
        
        assert account_id is not None


def test_get_account(app, base_account_data):
    with app.test_client() as client:
        # Create an account to retrieve
        response = client.post('/accounts', json=base_account_data)

        # Parse JSON string to a Python dict to get 'account_id
        account_id = json.loads(response.data)['account_id']

        response = client.get(f'/accounts/{account_id}')
        assert response.status_code == 200

        json_data = json.loads(response.data)

        assert json_data["_id"] == account_id
        assert json_data["first_name"] == base_account_data["first_name"]


def test_update_account(app, base_account_data):
    with app.test_client() as client:
        response = client.post('/accounts', json=base_account_data)
        account_id = json.loads(response.data)['account_id']

        update_data = {"first_name": "Lulu"}
        response = client.put(f'/accounts/{account_id}', json=update_data)
        assert response.status_code == 200
        
        json_data = json.loads(response.data)
        assert json_data["message"] == "Account updated successfully"