import requests
import os
from dotenv import load_dotenv
from flight_search import FlightSearch

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")

basic = requests.auth.HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASSWORD)


# This class is responsible for talking to the Google Sheet.
# def getData(self):
#     response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=basic)
class DataManager(FlightSearch):
    def __init__(self):
        super().__init__()
        self.sheet_data = []
        self.users_data = []
        self.get_sheety_api_data()
        self.get_users_data()

    def get_sheety_api_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=basic)
        response.raise_for_status()
        data = response.json()
        self.sheet_data = data["prices"]

    def get_sheet_data(self):
        return self.sheet_data

    def update_iata_codes(self):
        for item in self.sheet_data:
            iata_code = self.get_iata_code(item["city"])
            body = {"price": {"iataCode": iata_code}}
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{item['id']}", auth=basic, json=body
            )
            response.raise_for_status()
            print("IATA code successfully updated")

    def get_users_data(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, auth=basic)
        response.raise_for_status()
        self.users_data = response.json()["users"]
