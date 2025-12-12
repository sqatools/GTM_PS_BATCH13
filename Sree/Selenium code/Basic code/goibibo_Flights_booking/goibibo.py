import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://www.goibibo.com/")

driver.find_element(By.CSS_SELECTOR, ".logSprite.icClose").click()

time.sleep(3)

driver.find_element(By.XPATH, "//span[text()='From']/following::p[1]").click()

driver.find_element(By.XPATH, "(//p[text()='Mumbai, India'])[1]").click()

driver.find_element(By.XPATH, "//span[text()='To']/following::p[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "(//p[text()='Hyderabad, India'])[1]").click()
driver.find_element(By.XPATH,"//span[text()='Departure']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@aria-label='Tue Dec 15 2025']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[text()='Return']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@aria-label='Sat Dec 27 2025']").click()
time.sleep(2)
#Today=datetime.now()

##return_date = Today + timedelta(days=26).date()
driver.close()