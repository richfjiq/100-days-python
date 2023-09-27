# This class is responsible for talking to the Flight Search API.
import requests
import os
from dotenv import load_dotenv
from flight_data import FlightData

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

    def check_flights(
        self, origin_city_code, destination_city_code, from_time, to_time
    ):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

        response = requests.get(
            url=f"{TEQUILA_API}/v2/search", headers=headers, params=query
        )
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
            print(f"{destination_city_code}: £{data['price']}")
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
            )
            return flight_data
