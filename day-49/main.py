from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3726911628&f_AL=true&f_E=2&f_WT=2&geoId=101174742&keywords=react&location=Canada&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
)

login_button = driver.find_element(By.CLASS_NAME, value="nav__button-secondary")
login_button.click()

time.sleep(1)

username_input = driver.find_element(By.CSS_SELECTOR, value="input#username")
password_input = driver.find_element(By.CSS_SELECTOR, value="input#password")
# button_login = driver.find_element(
#     By.CSS_SELECTOR, value="div.login__form_action_container button"
# )

username_input.send_keys("rfjiqdevcode@gmail.com")
password_input.send_keys("Wd37N'2Su(55")
# button_login.click()
