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

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email_input = driver.find_element(By.XPATH, value='//*[@id="email"]')
password_input = driver.find_element(By.XPATH, value='//*[@id="pass"]')

email_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)

time.sleep(5)

allow_location = driver.find_element(
    By.XPATH,
    value='//*[@id="u-1622372915"]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]',
)
allow_location.click()

time.sleep(2)

enable_notifications = driver.find_element(
    By.XPATH,
    value='//*[@id="u-1622372915"]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]',
)
enable_notifications.click()

time.sleep(1)

accept_cookies = driver.find_element(
    By.XPATH, value='//*[@id="u106008161"]/div/div[2]/div/div/div[1]/div[1]/button'
)
accept_cookies.click()

for n in range(100):
    time.sleep(1)
    swift_left_button = driver.find_element(
        By.XPATH,
        value='//*[@id="u106008161"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]',
    )
    swift_left_button.click()

print("Bot finished 100 dislikes :)")
