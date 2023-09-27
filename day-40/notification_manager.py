import requests
import boto3
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")


class NotificationManager:
    def send_emails(
        self,
        price,
        departure_city_name,
        departure_iata_code,
        arrival_city_name,
        arrival_iata_code,
        outbound_date,
        inbound_date,
        user_email,
    ):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Make connection secure
            connection.starttls()
            connection.login(user=SMTP_EMAIL, password=SMTP_PASSWORD)
            connection.sendmail(
                from_addr=SMTP_EMAIL,
                to_addrs=user_email,
                msg=f"Subject:New Low Price Flight!\n\nLow price alert 🚨! Only £{price} to fly from London - {departure_iata_code} to {arrival_city_name} - {arrival_iata_code}, from {outbound_date} to {inbound_date}".encode(
                    "utf-8"
                ),
            )
