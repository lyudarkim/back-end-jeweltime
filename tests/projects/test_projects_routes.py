from flask import json


def test_create_project_route(app, base_account_data, base_project_data):
    with app.test_client() as client:
        account_response = client.post('/accounts', json=base_account_data)

        # Ensure the account creation is successful
        assert account_response.status_code == 201

        accountId = json.loads(account_response.data)['accountId']

        response = client.post(f'/projects', json=base_project_data)
        assert response.status_code == 201

        json_data = json.loads(response.data)
        projectId = json_data['projectId']
        json_data["accountId"] = accountId
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


def test_update_project_route_correctly_updates(app, base_account_data, base_project_data):
    with app.test_client() as client:
        # Create an account and project
        account_response = client.post('/accounts', json=base_account_data)
        accountId = json.loads(account_response.data)['accountId']

        project_response = client.post(f'/accounts/{accountId}/projects', json=base_project_data)
        projectId = json.loads(project_response.data)['projectId']

        # Update the created project
        updated_data = {"description": "Updated description"}
        update_response = client.put(f'/accounts/{accountId}/projects/{projectId}', json=updated_data)

        assert update_response.status_code == 200
        updated_project_data = json.loads(update_response.data)
        assert updated_project_data["description"] == updated_data["description"]
