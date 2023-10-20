from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
SIMILAR_ACCOUNT = "history"


class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://www.instagram.com/")

    def login(self):
        time.sleep(2)

        username_input = self.driver.find_element(
            By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input'
        )
        username_input.send_keys(USERNAME)

        password_input = self.driver.find_element(
            By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input'
        )
        password_input.send_keys(PASSWORD)

        login_button = self.driver.find_element(
            By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button'
        )
        login_button.click()

    def find_followers(self):
        time.sleep(5)

        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(3)

        followers_button = self.driver.find_elements(
            By.CSS_SELECTOR,
            value="header section ul li",
        )[1]
        followers_button.click()

    def follow(self):
        time.sleep(3)

        users = self.driver.find_elements(
            By.CSS_SELECTOR, value="button[class='_acan _acap _acas _aj1-']"
        )

        for user in users:
            try:
                user.click()
                time.sleep(8)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(
                    By.CSS_SELECTOR, value="button[class='_a9-- _a9_1']"
                )
                cancel.click()
