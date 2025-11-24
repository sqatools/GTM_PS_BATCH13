import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.booking.com/")
time.sleep(5)
driver.find_element(By.XPATH, "//button[@aria-label='Dismiss sign-in info.']").click()
driver.find_element(By.XPATH,"//span[contains(text(), 'Flight +')]").click()
driver.find_element(By.XPATH,"//span[contains(text(), 'Stays')]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div/span[text()='Car rental']").click()
driver.find_element(By.XPATH, "//span[text() = 'Cruises']").click()
driver.find_element(By.XPATH, "//span[@id='wthHeaderBannerCopy']").click()
driver.find_element(By.XPATH, "//button[@id='button-top-nav-0']").click()
driver.find_element(By.XPATH, "//span[@id='destinationText']").click()




