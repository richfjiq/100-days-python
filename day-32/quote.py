import smtplib
import datetime as dt
import random

MY_EMAIL = "rfjiqdevcode@gmail.com"
MY_PASSWORD = "qkosmxxqjrxpjczi"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        rand_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="rfjiqdevcode@yahoo.com",
            msg=f"Subject:Hello\n\n{rand_quote}".encode("utf-8"),
        )
