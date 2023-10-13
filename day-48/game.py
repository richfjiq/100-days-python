from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# +++++++++++++++++++++++ Getting items +++++++++++++++++++++++
cookie_button = driver.find_element(By.CSS_SELECTOR, value="#cookie")

timeout = time.time() + 5
five_min = time.time() + 60 * 5


def check_items_to_buy():
    money = driver.find_element(By.ID, value="money").text
    if "," in money:
        money = money.replace(",", "")
    money = int(money)
    store = driver.find_elements(By.CSS_SELECTOR, value="div#store div")

    # No need to check prices, game itself dont allow you to buy
    # items when there is no enough money

    # all_prices = driver.find_elements(By.CSS_SELECTOR, value="div#store b")
    # item_prices = []

    # for item in all_prices:
    #     item_text = item.text
    #     if item_text != "":
    #         cost = int(item_text.split("-")[1].strip().replace(",", ""))
    #         item_prices.append(cost)

    for i in range(len(store)):
        item_class = store[i].get_attribute("class")

        if item_class == "grayed":
            store[i - 1].click()
            break


while True:
    cookie_button.click()

    if time.time() > timeout:
        check_items_to_buy()
        timeout = time.time() + 5

    if time.time() > five_min:
        money = driver.find_element(By.CSS_SELECTOR, value="div#money").text
        print(money)
        break
