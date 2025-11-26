import time
from selenium import webdriver

from selenium .webdriver.common.by import By

#open browser

driver = webdriver.Chrome()
"""
driver.get("https://www.facebook.com")
# By ID locator
driver.find_element(By.ID, "email").send_keys("use@123")

driver.find_element(By.ID, "pass").send_keys("use@12345")

time.sleep(10)

driver.close()

"""




driver.maximize_window()

driver.implicitly_wait(10)
def opensource_website():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    time.sleep(10)
    driver.close()

opensource_website()





# By name locator


