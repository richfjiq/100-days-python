import requests
from twilio.rest import Client

api_key = "87c6e02bb713551cfe6a8cabf2015780"
account_sid = "AC7f84b9dce225f5810866c5c9b2caf96e"
auth_token = "bca2ff0276390a26fd72d425c7d9685b"

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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+15855952042",
        body="It's going to rain today. Remember to bring your ☔️",
        to="+527351258657",
    )
    print(message.status)
