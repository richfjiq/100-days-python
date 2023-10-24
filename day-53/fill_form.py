from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()

FORM_URL = os.getenv("FORM_URL")


class FillForm:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(FORM_URL)

    def fill(self, address, price, link):
        time.sleep(2)

        address_input = self.driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
        )
        address_input.send_keys(address)

        price_input = self.driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
        )
        price_input.send_keys(price)

        link_input = self.driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
        )
        link_input.send_keys(link)

        send_button = self.driver.find_element(
            By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
        )
        send_button.click()

        time.sleep(3)

        another_response = self.driver.find_element(
            By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a"
        )
        another_response.click()
