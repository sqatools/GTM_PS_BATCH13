import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# Set implicit timeout
driver.implicitly_wait(10)
# Maximize browser window
driver.maximize_window()

driver.get("https://sqatools.in/blogs/")

driver.find_element(By.ID,"email").send_keys("Latikap@gmail.com")
driver.find_element(By.CSS_SELECTOR,'#pass').send_keys("Pass@123")
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,"//button[normalize-space()='Create new account']").click()
