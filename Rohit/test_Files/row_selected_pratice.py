import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://sqatools.in/dummy-booking-website/")

checkboxes = driver.find_elements(By.XPATH,"//input[@value='checkbox']")

for ch in checkboxes:
    if not ch.is_selected():
        ch.click()
        time.sleep(2)
driver.quit()

