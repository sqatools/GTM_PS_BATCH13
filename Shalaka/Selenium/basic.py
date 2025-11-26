import time
from selenium import webdriver

from selenium .webdriver.common.by import By

#open browser

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://www.facebook.com")

driver.find_element(By.ID, "email").send_keys("use@123")

driver.find_element(By.ID, "pass").send_keys("use@12345")

time.sleep(10)

driver.close()
