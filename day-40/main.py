import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")

basic = requests.auth.HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASSWORD)


def create_user(first_name, last_name, email):
    body = {"user": {"firstName": first_name, "lastName": last_name, "email": email}}
    response = requests.post(url=SHEETY_USERS_ENDPOINT, auth=basic, json=body)
    response.raise_for_status()
    print("User created in Flight Deals Google Sheet")


def user_data():
    print(
        "Welcome to Ricardo's Flight Club\nWe find the best flights deals and email you,"
    )
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    email = input("What is your email?\n")
    confirm_email = input("Type your email.\n")
    if email != confirm_email:
        confirm_email = input("Email must match, please type your email again.\n")
    print("You're in the club!\n\n")
    create_user(first_name=first_name, last_name=last_name, email=email)


active_program = True

while active_program:
    user_data()
    run_again = input("This program has exited, run again? yes / no\n")
    if run_again.lower() == "no":
        active_program = False
