from flask import json


def test_create_project(app, base_account_data, base_project_data):
    with app.test_client() as client:
        account_response = client.post('/accounts', json=base_account_data)
        account_id = json.loads(account_response.data)['account_id']

        response = client.post(f'/accounts/{account_id}/projects', json=base_project_data)

        assert response.status_code == 201

        json_data = json.loads(response.data)
        project_id = json_data['project_id']
        assert project_id is not None


def test_get_project(app, base_account_data, base_project_data):
    with app.test_client() as client:
        account_response = client.post('/accounts', json=base_account_data)
        account_id = json.loads(account_response.data)['account_id']

        response = client.post(f'/accounts/{account_id}/projects', json=base_project_data)
        project_id = json.loads(response.data)['project_id']
        
        response = client.get(f'/accounts/{account_id}/projects/{project_id}')
        assert response.status_code == 200

        json_data = json.loads(response.data)
        assert json_data["_id"] == project_id
        assert json_data["description"] == base_project_data["description"]
