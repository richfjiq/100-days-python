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
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.speedtest.net/")

        time.sleep(3)

        go_button = driver.find_element(
            By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a',
        )
        go_button.click()

        time.sleep(42)

        speed_down = driver.find_element(
            By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span',
        ).text
        down = speed_down

        speed_up = driver.find_element(
            By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span',
        ).text
        up = speed_up

        driver.quit()

    def tweet_at_provider(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://twitter.com/i/flow/login")

        time.sleep(3)

        email_input = driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input',
        )
        email_input.send_keys(TWITTER_EMAIL)

        next_button = driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]',
        )
        next_button.click()

        time.sleep(3)

        username_input = driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input',
        )
        username_input.send_keys(TWITTER_USERNAME)

        second_next_button = driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div',
        )
        second_next_button.click()

        time.sleep(3)

        password_input = driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input',
        )
        password_input.send_keys(TWITTER_PASSWORD)

        login_button = driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div',
        )
        login_button.click()

        time.sleep(2)

        new_twitter_modal = driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div',
        )
        new_twitter_modal.click()

        time.sleep(1)

        textarea = driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div',
        )
        textarea.send_keys(
            f"Hey @izzi_mx, Why is my internet speed {self.down} down / {self.up} up when I paid for 100 down / 10 up?"
        )

        post_twitter = driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]',
        )
        post_twitter.click()

        time.sleep(2)

        driver.quit()
