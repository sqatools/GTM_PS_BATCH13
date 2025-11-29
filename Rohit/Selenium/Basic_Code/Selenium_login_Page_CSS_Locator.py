import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://sqatools.in/dummy-booking-website/")

driver.find_element(By.LINK_TEXT, "Login Page").click()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email address or phone number']").send_keys("karad12@gamil.com")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("Karad@123")
driver.find_element(By.CSS_SELECTOR, "button[id='loginbutton']").click()

time.sleep(10)
driver.close()