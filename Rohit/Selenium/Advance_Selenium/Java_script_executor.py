import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/dummy-booking-website/")

fromcity_elem =  driver.execute_script("return document.getElementById('fromcity')")
fromcity_elem.send_keys("Karad")
destcity_elem = driver.execute_script("return document.getElementById('destcity');")
destcity_elem.send_keys("Mumbai")
time.sleep(5)

title = driver.execute_script("return document.title")
print("website title :", title)
URL = driver.execute_script("return document.URL")
print("current URL:", URL)

window_height = driver.execute_script("return window.outerHeight")
print("Windown height :", window_height)
window_width = driver.execute_script("return window.outerWidth")
print("Window width :", window_width)
time.sleep(5)

# scroll to height of the page.
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

driver.close()