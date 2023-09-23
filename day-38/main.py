import requests

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


response = requests.post(url=nutritionixt_endpoint, headers=headers, json=params)
response.raise_for_status()

data = response.json()
print(data)
