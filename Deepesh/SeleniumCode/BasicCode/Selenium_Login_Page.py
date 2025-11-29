import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://sqatools.in/dummy-booking-website/")
driver.find_element(By.LINK_TEXT, "Login Page").click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Email address or phone number']").send_keys("testuser@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("user@12345")
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()
time.sleep(5)
driver.close()