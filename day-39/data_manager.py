import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")

basic = requests.auth.HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASSWORD)


# This class is responsible for talking to the Google Sheet.
# def getData(self):
#     response = requests.get(url=SHEETY_ENDPOINT, auth=basic)
class DataManager:
    def __init__(self):
        self.data = []
        self.getData()

    def getData(self):
        response = requests.get(url=SHEETY_ENDPOINT, auth=basic)
        response.raise_for_status()
        self.data = response.json()

    def getCitiesData(self):
        return self.data
