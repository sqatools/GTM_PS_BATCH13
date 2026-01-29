import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.facebook.com/")

driver.find_element(By.XPATH,"//input[@placeholder='Email address or phone number']").send_keys("rohitramchandrachavan@gmail.com")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("Samartha@123")
driver.find_element(By.XPATH,"//button[text()='Log in']").click()
time.sleep(3)

driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
driver.find_element(By.XPATH, "//input[@aria-label='First name']").send_keys("Mahesh")
driver.find_element(By.XPATH, "//input[@aria-label='Surname']").send_keys("More")
driver.find_element(By.NAME, "birthday_day").send_keys("18")
time.sleep(5)