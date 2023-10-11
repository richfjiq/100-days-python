from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# +++++++++++++++++++++++ Getting inputs +++++++++++++++++++++++
first_name_input = driver.find_element(By.NAME, value="fName")
last_name_input = driver.find_element(By.NAME, value="lName")
email_input = driver.find_element(By.NAME, value="email")

# +++++++++++++++++++++++ Submit button +++++++++++++++++++++++
submit_form = driver.find_element(By.CSS_SELECTOR, value="form button")

# +++++++++++++++++++++++ Typing data in inputs +++++++++++++++++++++++
first_name_input.send_keys("Billy")
last_name_input.send_keys("The Kid")
email_input.send_keys("billy@test.com")

# +++++++++++++++++++++++ Submit data +++++++++++++++++++++++
submit_form.send_keys(Keys.ENTER)

# driver.quit()
