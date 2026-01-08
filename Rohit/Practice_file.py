import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver =  webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)



def Test_login():
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.NAME, "username").send_keys("student")
    driver.find_element(By.NAME, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(5)


Test_login()
