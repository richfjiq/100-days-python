# This class is responsible for talking to the Flight Search API.
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TEQUILA_API = os.getenv("TEQUILA_API")
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")


class FlightSearch:
    def get_iata_code(self, city_name):
        locations_endpoint = f"{TEQUILA_API}/locations/query"
        query = {"term": city_name, "location_types": "city"}
        headers = {"apikey": TEQUILA_API_KEY}
        response = requests.get(url=locations_endpoint, headers=headers, params=query)
        response.raise_for_status()
        data = response.json()
        city_info = data["locations"][0]
        return city_info["code"]
