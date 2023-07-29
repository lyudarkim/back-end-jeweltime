from flask import json


def test_create_project(app, base_account_data, base_project_data):
    with app.test_client() as client:
        account_response = client.post('/accounts', json=base_account_data)
        accountId = json.loads(account_response.data)['accountId']

        response = client.post(f'/accounts/{accountId}/projects', json=base_project_data)

        assert response.status_code == 201

        json_data = json.loads(response.data)
        projectId = json_data['projectId']
        assert projectId is not None


def test_get_project(app, base_account_data, base_project_data):
    with app.test_client() as client:
        account_response = client.post('/accounts', json=base_account_data)
        accountId = json.loads(account_response.data)['accountId']

        response = client.post(f'/accounts/{accountId}/projects', json=base_project_data)
        projectId = json.loads(response.data)['projectId']
        
        response = client.get(f'/accounts/{accountId}/projects/{projectId}')
        assert response.status_code == 200

        json_data = json.loads(response.data)
        assert json_data["_id"] == projectId
        assert json_data["description"] == base_project_data["description"]
