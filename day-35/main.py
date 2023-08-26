import requests

api_key = "87c6e02bb713551cfe6a8cabf2015780"
parameters = {
    # "lat": 18.811810,
    "lat": 18.883810,
    # "lon": -98.955093,
    "lon": -96.952080,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}
response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall", params=parameters
)
response.raise_for_status()
weather_data = response.json()
next_twelve_hours = [n["weather"][0]["id"] for n in weather_data["hourly"][0:12]]
will_rain = False
for code in next_twelve_hours:
    if code < 700:
        will_rain = True
if will_rain:
    print("Bring a weather")
