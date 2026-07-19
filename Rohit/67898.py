import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")

user_name = driver.find_element(By.XPATH,"//input[@id='username']").send_keys("student")
password = driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Password123")
submit = driver.find_element(By.XPATH,"//button[text()='Submit']").click()
time.sleep(5)
driver.close()
