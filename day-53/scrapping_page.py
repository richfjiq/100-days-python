import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

OPENRENT_URL = os.getenv("OPENRENT_URL")
BASE_URL = os.getenv("BASE_URL")

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9",
}


class Scrapping:
    def __init__(self):
        self.scrapping_page()
        self.prices = []
        self.links = []
        self.addresses = []

    def scrapping_page(self):
        response = requests.get(url=OPENRENT_URL, headers=header)
        openrent_page = response.content
        soup = BeautifulSoup(openrent_page, "html.parser")

        soup_links = soup.find_all("a", class_="pli clearfix")
        self.links = [link["href"] for link in soup_links]

        soup_prices = soup.find_all("div", class_="pim pl-title")
        self.prices = [
            price.h2.getText().strip().split(" ")[0] for price in soup_prices
        ]

        soup_addresses = soup.find_all("span", class_="banda pt listing-title")
        self.addresses = [
            address.getText().split(",")[1].strip() for address in soup_addresses
        ]
