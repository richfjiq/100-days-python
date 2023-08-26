import requests
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

api_key = "87c6e02bb713551cfe6a8cabf2015780"

sns_client = boto3.client(
    "sns",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)


parameters = {
    "lat": 18.883810,
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
    message = sns_client.publish(
        PhoneNumber="+527351258657",
        Message="It's going to rain today. Remember to bring your ☔️",
        # TopicArn="arn:aws:sns:us-east-1:323973364280:weather-alarm",
    )
    print(f"Status Code: {message['ResponseMetadata']['HTTPStatusCode']}")
