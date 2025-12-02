import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.goibibo.com")

# Close popup
driver.find_element(By.XPATH, "//span[@class='logSprite icClose']").click()

# FROM City
city_name = driver.find_element(By.XPATH, "//label[@for='fromCity']")
city_name.click()
time.sleep(3)
city_name.send_keys("Mumbai")

boarding_name = driver.find_element(By.XPATH, "//div[@role='combobox']")
boarding_name.find_element(By.XPATH, "//*[text()='BOM']").click()

# TO City
to_city = driver.find_element(By.XPATH, "//label[@for='toCity']")
to_city.click()
time.sleep(2)

to_input = driver.find_element(By.ID, "toCity")
to_input.send_keys("PNQ")

# Explicit wait for dropdown option
wait = WebDriverWait(driver, 10)

going_city = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='PNQ']")))
going_city.click()
time.sleep(5)

# Select departure date
depart_date = driver.find_element(By.XPATH,"//div[@aria-label='Thu Dec 18 2025']")
depart_date.click()
time.sleep(5)

# Select landing date
cal_return = driver.find_element(By.XPATH,"//span[text()='Return']")
cal_return.click()
departing_day = "Thu Jan 01 2026"
landing_date = driver.find_element(By.XPATH,f"//div[@aria-label='{departing_day}']")
landing_date.click()
time.sleep(5)

# Select travellers class
driver.find_element(By.XPATH, "//span[text()='Travellers & Class']").click()
time.sleep(5)
age = driver.find_element(By.XPATH,"(//ul[@class='guestCounter font12 darkText gbCounter'])[1]")
driver.find_element(By.XPATH, "//li[@data-cy='adults-3']").click()
time.sleep(3)

#CHOOSE TRAVEL CLASS
travel_class = driver.find_element(By.XPATH, "//li[text()='Premium Economy']")
travel_class.click()
time.sleep(3)

# Apply Button
apply_button = driver.find_element(By.XPATH, "//button[@type='button']")
apply_button.click()
time.sleep(3)


