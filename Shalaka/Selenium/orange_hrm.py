import time
from selenium import webdriver

from selenium .webdriver.common.by import By

#open browser

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(3)
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)

driver.find_element(By.XPATH, "//h6[text()= 'Dashboard']")
print("Page Title", driver.title)

driver.find_element(By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']").click()
time.sleep(5)

#Add Data
driver.find_element(By.XPATH, "//button[text()=' Add ']").click()
time.sleep(5)
driver.find_element(By.XPATH, "(//div[text()='-- Select --'])[1]").click()

