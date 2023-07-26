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
        "zipcode": "98104",
    }

@pytest.fixture
def account_schema():
    return AccountSchema()


# Fixtures for ProjectSchema
@pytest.fixture
def base_project_data():
    return {
        "project_name": "Keum-boo pendant with garnet",
        "description": "Small round silver pendant with a flush set garnet",
        "account_id": "759ac5f0377b7ec8bcf7f3ce4fd8e915142d6f5164821922",
        "project_id": "7",  
        "started_at": "2021-08-21",  # ISO 8601 format
        "completed_at": "2021-08-24", 
        "hours_spent": 4.0,
        "materials_cost": 79.0,
        "metals": ["sterling silver 20ga sheet", "24K gold foil"],
        "gemstones": ["flush set round brilliant garnet"],
        "notes": [
            "Messed up the SS disc when cutting it out but it turned out to be a really cool texture and a feature of the pendant.", 
            "Was going to set a 3 mm stone but ended up using the 5 mm garnet because I kept messing up the setting"
        ],
        "shape": "round",
        "jewelry_type": "pendant",
    }


@pytest.fixture
def invalid_project_data():
    return {
        "project_name": "Statement bracelet with agate",
        "description": "Oversized gold and silver bracelet with an oval agate",
        "account_id": "759ac5f0377b7ec8bcf7f3ce4fd8e915142d6f5164821922",
        "started_at": "2021-08-25",  # This is after the completion date
        "completed_at": "2021-08-24",
        "hours_spent": 10,
        "materials_cost": 300.95,
        "materials": ["18K yellow gold jump rings", "paste solder"],
        "metals": ["sterling silver 16ga sheet", "18K gold sheet 20ga", "Shibuichi alloy from ShiningMetals.com 18ga sheet"],
        "gemstones": ["bezel set oval cabochon agate"],
        "notes": [
            "Due to the size of the bracelet, I struggled with soldering it. Needed to use the biggest torch tip.", 
        ],
        "shape": "irregular",
        "jewelry_type": "bracelet",
    }


@pytest.fixture
def project_schema():
    return ProjectSchema()
