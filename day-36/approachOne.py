import requests
import boto3
import os
from dotenv import load_dotenv
import datetime as dt

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
RAISE_PERCENTAGE = 2
FALL_PERCENTAGE = 5

parameters_news = {
    "q": "(tesla OR Tesla OR Musk)",
    "from": "2023-08-24",
    "to": "2023-08-25",
    "language": "en",
    "pageSize": 3,
    "apiKey": os.getenv("NEWS_API_KEY"),
}

parameters_stock_market = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.getenv("ALPHA_VANTAGE_API_KEY"),
}

today = dt.date.today()
yesterday = today - dt.timedelta(days=1)
before_yesterday = today - dt.timedelta(days=2)

response_news = requests.get(url=os.getenv("NEWS_API_URL"), params=parameters_news)
response_news.raise_for_status()
news_data = response_news.json()["articles"]

sns_client = boto3.client(
    "sns",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

response_stock_market = requests.get(
    url=os.getenv("ALPHA_VANTAGE_API_URL"), params=parameters_stock_market
)
response_stock_market.raise_for_status()
stock_market_data = response_stock_market.json()["Time Series (Daily)"]
market_close_yesterday = float(stock_market_data[f"{yesterday}"]["4. close"])
market_close_before_yesterday = float(
    stock_market_data[f"{before_yesterday}"]["4. close"]
)
fall_or_raise = (
    (market_close_yesterday - market_close_before_yesterday) / market_close_yesterday
) * 100

if fall_or_raise >= 2:
    for new in news_data:
        message = (
            f"{STOCK} 🔺 2 %\nHeadline: {new['title']}\nBrief: {new['description']}"
        )
        response = sns_client.publish(PhoneNumber="+527351258657", Message=message)
        print(f"Status Code: {response['ResponseMetadata']['HTTPStatusCode']}")
if fall_or_raise < -5:
    for new in news_data:
        message = (
            f"{STOCK} 🔻 5 %\nHeadline: {new['title']}\nBrief: {new['description']}"
        )
        response = sns_client.publish(PhoneNumber="+527351258657", Message=message)
        print(f"Status Code: {response['ResponseMetadata']['HTTPStatusCode']}")


# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=H7GSR3J657QH9VKZ


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
