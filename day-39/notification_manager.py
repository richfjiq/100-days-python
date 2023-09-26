import requests
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

sns_client = boto3.client(
    "sns",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)


class NotificationManager:
    def send_notification(
        self,
        price,
        departure_city_name,
        departure_iata_code,
        arrival_city_name,
        arrival_iata_code,
        outbound_date,
        inbound_date,
    ):
        message = f"Low price alert 🚨! Only £{price} to fly from London - {departure_iata_code} to {arrival_city_name} - {arrival_iata_code}, from {outbound_date} to {inbound_date}"
        response = sns_client.publish(PhoneNumber="+527351258657", Message=message)
        print(f"Status Code: {response['ResponseMetadata']['HTTPStatusCode']}")
