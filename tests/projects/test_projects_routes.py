from flask import json


def test_create_project_route(app, base_account_data, base_project_data):
    with app.test_client() as client:
        account_response = client.post('/accounts', json=base_account_data)
        accountId = json.loads(account_response.data)['accountId']

        response = client.post(f'/accounts/{accountId}/projects', json=base_project_data)

        assert response.status_code == 201

        json_data = json.loads(response.data)
        projectId = json_data['projectId']
        assert projectId is not None


def test_get_project_route(app, base_account_data, base_project_data):
    with app.test_client() as client:
        account_response = client.post('/accounts', json=base_account_data)
        accountId = json.loads(account_response.data)['accountId']

        response = client.post(f'/accounts/{accountId}/projects', json=base_project_data)
        projectId = json.loads(response.data)['projectId']
        
        response = client.get(f'/accounts/{accountId}/projects/{projectId}')
        assert response.status_code == 200

        json_data = json.loads(response.data)
        assert json_data["description"] == base_project_data["description"]


def test_get_all_projects_route(app, base_account_data, base_project_data):
    with app.test_client() as client:
        account_response = client.post('/accounts', json=base_account_data)
        accountId = json.loads(account_response.data)['accountId']

        base_project_data["accountId"] = accountId

        # Make POST requests for two projects
        response_1 = client.post(f'/accounts/{accountId}/projects', json=base_project_data.copy())
        response_2 = client.post(f'/accounts/{accountId}/projects', json=base_project_data.copy())

        project_1 = json.loads(response_1.data)
        project_2 = json.loads(response_2.data)
        assert "projectId" in project_1
        assert "projectId" in project_2

        response = client.get(f'/accounts/{accountId}/projects')
        assert response.status_code == 200

        json_data = json.loads(response.data)
        assert len(json_data) == 2, "Not all projects retrieved"

        for project in json_data:
            assert project["accountId"] == accountId
            assert project["description"] == base_project_data["description"]
