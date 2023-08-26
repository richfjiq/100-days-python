import requests

api_key = "87c6e02bb713551cfe6a8cabf2015780"
parameters = {"lat": 18.811810, "lon": -98.955093, "appid": api_key}
response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall", params=parameters
)
response.raise_for_status()
print(response.status_code)
data = response.json()
print(data)
