from flask import json
from application.modules.accounts.routes import (
    create_account, 

)


def test_create_account(app, base_account_data):
    with app.test_client() as client:
        response = client.post('/accounts', json=base_account_data)

        assert response.status_code == 201

        # Convert raw data into a Python dictionary
        json_data = json.loads(response.data)
        account_id = json_data['account_id']
        
        assert account_id is not None