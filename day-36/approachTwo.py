import requests
import boto3
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = os.getenv("ALPHA_VANTAGE_API_URL")
NEWS_ENDPOINT = os.getenv("NEWS_API_URL")

STOCK_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(
    float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
)

diff_percent = (difference / float(yesterday_closing_price)) * 100

if diff_percent > 2:
    print("Get news")
