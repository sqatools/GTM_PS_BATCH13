import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = "firefox"

driver= None
if browser.lower() == 'chrome':
    driver = webdriver.Chrome()
elif browser.lower() == 'firefox':
    driver = webdriver.Firefox()
elif browser.lower() == "edge":
    driver = webdriver.Edge()


driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.booking.com/")
time.sleep(10)
# close the registration popup
try:
    driver.find_element(By.XPATH, "//button[@aria-label='Dismiss sign-in info.']").click()
except Exception as e:
    print(e)

input_field = driver.find_element(By.XPATH, "//input[@aria-label='Where are you going?']")
# search city name
input_field.click()
time.sleep(3)
input_field.send_keys("Mumbai")
# select city option from list of options
option = driver.find_element(By.XPATH, "//div[text()='Mumbai']//ancestor::li")
option.screenshot("option_snap.png")
option.click()

time.sleep(5)
driver.close()


