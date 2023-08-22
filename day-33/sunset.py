import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "rfjiqdevcode@gmail.com"
PASSWORD = "qkosmxxqjrxpjczi"

MY_LAT = 18.811810
MY_LONG = -98.955093


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_data = iss_response.json()
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])

    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True


def is_night():
    parameters = {"lat": MY_LAT, "long": MY_LONG, "formatted": 0}

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now.hour >= sunset and time_now.hour < sunrise:
        return True
    return False


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="rfjiqdevcode@yahoo.com",
            msg="Subject:Hey look up\n\nNow is the time, look up.",
        )


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        send_email()
