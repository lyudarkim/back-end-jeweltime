import pytest
from application.modules.accounts.validators import AccountSchema
from application.modules.projects.validators import ProjectSchema


# Fixtures for AccountSchema
@pytest.fixture
def base_account_data():
    return {
        "first_name": "Juniper",
        "last_name": "Moon",
        "email": "juniper.moon@gmail.com",
        "zipcode": "98104"
    }

@pytest.fixture
def account_schema():
    return AccountSchema()


# Fixtures for ProjectSchema
@pytest.fixture
def base_project_data():
    return {
        "project_name": "Keum-boo pendant with garnet",
        "project_id": "7",  
        "started_at": "2021-08-21T00:00:00",  # ISO 8601 format
        "completed_at": "2021-08-24T00:00:00", 
        "hours_spent": 4.0,
        "materials_cost": 79.0,
        "metals": [
            {
                "type": "gold",
                "form": "foil",
                "karat": "24K",
            },
            {
                "type": "silver",
                "form": "sheet",
                "alloy": "sterling", 
                "thickness": ["20ga", 0.8]
            }
        ],
        "commission": False,
        "unique": True,
        "gemstones": ["garnet", 1, "round", "brilliant", "flush set",  5],
        "jewelry_type": "pendant",
        "shape": "round",
    }


@pytest.fixture
def project_schema():
    return ProjectSchema()
