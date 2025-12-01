import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



browser = "edge"
driver = None

if browser == "chrome":
    driver = webdriver.Chrome()
elif browser == "firefox":
    driver = webdriver.Firefox()
elif browser == "edge":
    driver = webdriver.Edge()

driver.minimize_window()
driver.implicitly_wait(5)
driver.get("https://www.booking.com/")
time.sleep(10)
try:
    driver.find_element(By.XPATH, "//button[@aria-label='Dismiss sign-in info.']").click()
except Exception as e:

 input_field = driver.find_element(By.XPATH, "//input[@placeholder='Where are you going?']")
# search city name
 input_field.click()
 time.sleep(5)
 input_field.send_keys("Mumbai")

# select city option from list of options
option = driver.find_element(By.XPATH,"//div[text()='Mumbai']//ancestor::li")
option.screenshot("option2_snap.png")
option.click()

time.sleep(10)
driver.close()