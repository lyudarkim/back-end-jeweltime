import requests


METALS_API_URL = "https://api.metals.live/v1/spot"


def get_metal_prices():
    response = requests.get(METALS_API_URL)

    if response.status_code != 200:
        raise requests.RequestException(f"Failed to get metal prices. Status Code: {response.status_code}")
    
    return response.json()
