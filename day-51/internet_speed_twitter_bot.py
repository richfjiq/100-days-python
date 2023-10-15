from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = os.getenv("PROMISED_DOWN")
PROMISED_UP = os.getenv("PROMISED_UP")
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # time.sleep(1)

        go_button = self.driver.find_element(
            By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a',
        )
        go_button.click()

        time.sleep(42)

        speed_down = self.driver.find_element(
            By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span',
        ).text

        print(f"download speed: {speed_down}")

        speed_up = self.driver.find_element(
            By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span',
        ).text

        print(f"upload speed: {speed_up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")

        time.sleep(3)

        email_input = self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input',
        )
        email_input.send_keys(TWITTER_EMAIL)

        next_button = self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]',
        )
        next_button.click()

        time.sleep(3)

        username_input = self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input',
        )
        username_input.send_keys(TWITTER_USERNAME)

        second_next_button = self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div',
        )
        second_next_button.click()

        time.sleep(3)

        password_input = self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input',
        )
        password_input.send_keys(TWITTER_PASSWORD)

        login_button = self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div',
        )
        login_button.click()
