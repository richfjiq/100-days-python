from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


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

        time.sleep(4)

        notifications_off = self.driver.find_element(
            By.XPATH,
            value="/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]",
        )
        notifications_off.click()

    def find_followers(self):
        pass

    def follow(self):
        pass
