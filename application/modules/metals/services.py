import requests


METALS_API_URL = "https://api.metals.live/v1/spot"


def service_get_metal_prices():
    response = requests.get(METALS_API_URL)

    # If the request fails, it will raise a 'requests.RequestException'
    response.raise_for_status()
    
    return response.json()
