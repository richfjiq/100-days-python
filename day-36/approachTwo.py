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

news_params = {
    "apiKey": os.getenv("NEWS_API_KEY"),
    "qInTitle": COMPANY_NAME,
}

sns_client = boto3.client(
    "sns",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

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

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_percent) > 1:
    # print("Get news")
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles
    ]

    for article in formatted_articles:
        response = sns_client.publish(PhoneNumber="+527351258657", Message=article)
        print(f"Status Code: {response['ResponseMetadata']['HTTPStatusCode']}")
