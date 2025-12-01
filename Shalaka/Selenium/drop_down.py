import time
from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.support.select import Select

#open browser

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://www.goibibo.com")

driver.find_element(By.XPATH, "//span[@class='logSprite icClose']").click()
time.sleep(10)
city_name = driver.find_element(By.XPATH, "//label[@for='fromCity']")
city_name.click()
time.sleep(3)
city_name.send_keys("Mumbai")
time.sleep(3)
boarding_name = driver.find_element(By.XPATH, "//div[@role='combobox']")
boarding_name.find_element(By.XPATH, "//*[text()='BOM']").click()
time.sleep(10)

to_city = driver.find_element(By.XPATH, "//label[@for='toCity']")
to_city.click()
time.sleep(3)
city_name.send_keys("Delhi")
going_city = driver.find_element(By.XPATH, "//input[@id='toCity']")
going_city.find_element(By.XPATH, "//*[text()='New Delhi, India']")
going_city.click()

#city = Select(going_city)
#city.select_by_index(3)
time.sleep(10)


