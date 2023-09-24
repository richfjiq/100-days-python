import requests
from datetime import datetime

APP_ID = "14e098eb"
API_KEY = "53bb2651eaddd9d9d38f9ed48cd5cd3c"

nutritionixt_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {"x-app-id": APP_ID, "x-app-key": API_KEY, "x-remote-user-id": "0"}

GENDER = "male"
WEIGHT_KG = 78
HEIGHT_CM = 169
AGE = 37

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

response = requests.post(url=nutritionixt_endpoint, headers=headers, json=params)
response.raise_for_status()
data = response.json()

sheety_endpoint = (
    "https://api.sheety.co/9be0467a8435c8ea87080d818f18feac/workoutTracking/workouts"
)
SHEETY_USERNAME = "rich86workouts"
SHEETY_PASSWORD = "dB2d}9XR0/p]"

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
    response = requests.post(url=sheety_endpoint, auth=basic, json=body)
    response.raise_for_status()
    print("Successfully posted :)")
