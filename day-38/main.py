import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

NUTRITIONIXT_APP_ID = os.getenv("NUTRITIONIXT_APP_ID")
NUTRITIONIXT_API_KEY = os.getenv("NUTRITIONIXT_API_KEY")
NUTRITIONIXT_ENDPOINT = os.getenv("NUTRITIONIXT_ENDPOINT")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")
GENDER = "male"
WEIGHT_KG = 78
HEIGHT_CM = 169
AGE = 37

headers = {
    "x-app-id": NUTRITIONIXT_APP_ID,
    "x-app-key": NUTRITIONIXT_API_KEY,
    "x-remote-user-id": "0",
}

query = input("Tell me which exercises you did: ")

params = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.time().strftime("%H:%M:%S")

response = requests.post(url=NUTRITIONIXT_ENDPOINT, headers=headers, json=params)
response.raise_for_status()
data = response.json()

basic = requests.auth.HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASSWORD)

for item in data["exercises"]:
    body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": item["user_input"].title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"],
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, auth=basic, json=body)
    response.raise_for_status()
    print("Successfully posted :)")
