import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://sqatools.in/dummy-booking-website/")
driver.find_element(By.LINK_TEXT, "Login Page").click()
time.sleep(3)

browser_winds = driver.window_handles
print(browser_winds)
driver.switch_to.window(browser_winds[1])

driver.find_element(By.ID, "email").send_keys("user1@gmail.com")
driver.find_element(By.ID, "pass").send_keys("user@12345")
time.sleep(5)
driver.find_element(By.ID, "loginbutton").click()

#Toggle bw tabs

driver.switch_to.window(browser_winds[0])
Title = driver.find_element(By.TAG_NAME, "h1")
print("Title :", Title.text)

time.sleep(5)

driver.close()
