from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "rfiq1986@hotmail.com"
PASSWORD = "07xb9My30a&"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

time.sleep(2)

login_button = driver.find_element(
    By.XPATH,
    value='//*[@id="u106008161"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a',
)
login_button.click()

time.sleep(2)

login_facebook_button = driver.find_element(
    By.XPATH,
    value='//*[@id="u-1622372915"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]',
)
login_facebook_button.click()

time.sleep(2)

email_input = driver.find_element(
    By.CSS_SELECTOR, value="div[id='email_container div input']"
)
password_input = driver.find_element(
    By.CSS_SELECTOR, value="div[class='clearfix form_row'] div input[id='pass']"
)
login_facebook_modal = driver.find_element(
    By.CSS_SELECTOR, value="div[id='buttons'] label input"
)

email_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD)
login_facebook_modal.click()
