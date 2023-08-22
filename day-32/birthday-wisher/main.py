import smtplib
import datetime as dt
import pandas
import random

MY_EMAIL = "rfjiqdevcode@gmail.com"
MY_PASSWORD = "qkosmxxqjrxpjczi"

now = dt.datetime.now()
weekday = now.day
month = now.month

data = pandas.read_csv("birthdays.csv")
birthdays_data = data.to_dict(orient="records")
for birthday in birthdays_data:
    birthday_day = birthday["day"]
    birthday_month = birthday["month"]

    if month == birthday_month and weekday == birthday_day:
        rand_letter = random.randint(1, 3)
        with open(f"./letter_templates/letter_{rand_letter}.txt") as file:
            letter = file.read()
            letter_edited = letter.replace("[NAME]", f"{birthday['name']}")
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday["email"],
                msg=f"Subject:Happy Birthday :)\n\n{letter_edited}",
            )
