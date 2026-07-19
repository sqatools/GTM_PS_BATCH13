import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")

user_name =driver.find_element(By.XPATH,"//input[@name='username']").send_keys("student")
psd = driver.find_element(By.XPATH,"//input[contains(@id,'password')]").send_keys("Password123")
submit_btn = driver.find_element(By.XPATH,"//button[text()='Submit']").click()

time.sleep(5)

driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)

driver.refresh()
time.sleep(5)
driver.close()