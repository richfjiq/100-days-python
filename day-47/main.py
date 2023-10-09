import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import lxml
import smtplib

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")

# AMAZON_URL = os.getenv("AMAZON_URL")
# USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
# ACCEPT_LANGUAGE = "es-US,es-419;q=0.9"
# # ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"

# response = requests.get(
#     # url=AMAZON_URL,
#     url="https://www.costco.com.mx/Electronicos/Apple/iPhone/Apple-iPhone-14-Pro-Max-128GB-Morado-Oscuro/p/676875",
#     # headers={
#     #     "accept-language": "en-US,en;q=0.9",
#     #     "accept-encoding": "gzip, deflate, br",
#     #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
#     #     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     # }
#     # headers={
#     #     "User-Agent": USER_AGENT,
#     #     "Accept-Language": ACCEPT_LANGUAGE,
#     #     # "accept": ACCEPT,
#     # },
# )
# amazon_page = response.text
# soup = BeautifulSoup(amazon_page, "html.parser")
# # price = soup.find(class_="a-price-whole")
# print(soup)

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

if price_as_float < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="rfiq1986@hotmail.com",
            msg=f"Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Sauté, Yogurt Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, 3 Quart is now ${price_as_float}".encode(
                "utf-8"
            ),
        )
