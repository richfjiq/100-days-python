import smtplib

my_email = "rfjiqdevcode@gmail.com"
password = "qkosmxxqjrxpjczi"


with smtplib.SMTP("smtp.gmail.com") as connection:
    # Make connection secure
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="rfjiqdevcode@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email",
    )

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1986, month=7, day=7)
# print(date_of_birth)
