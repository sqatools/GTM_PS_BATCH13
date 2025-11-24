from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element(By.NAME, "username").send_keys("Admin")
print("User name added")
driver.find_element(By.NAME, "password").send_keys("admin123")
print("Password added")