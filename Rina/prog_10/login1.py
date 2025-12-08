"""
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH, "//input[@name='username']")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@type='password')")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@tye='submit']")
time.sleep(2)

driver.close()

"""