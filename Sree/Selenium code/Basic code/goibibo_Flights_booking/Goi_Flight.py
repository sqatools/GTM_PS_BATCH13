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
# Explicit wait for dropdown option
wait = WebDriverWait(driver, 10)


def close_popup():
    # Close popup
    driver.find_element(By.XPATH, "//span[@class='logSprite icClose']").click()


def select_from_city():
    # FROM City
    From_city = driver.find_element(By.XPATH, "//label[@for='fromCity']")
    From_city.click()
    time.sleep(3)
    From_city.send_keys("Mumbai")

    boarding_name = driver.find_element(By.XPATH, "//div[@role='combobox']")
    boarding_name.find_element(By.XPATH, "//*[text()='BOM']").click()


def select_to_city():
    # TO City
    to_city = driver.find_element(By.XPATH, "//label[@for='toCity']")
    to_city.click()
    time.sleep(2)
    to_input = driver.find_element(By.ID, "toCity")
    to_input.send_keys("PNQ")

    going_city = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='PNQ']")))
    going_city.click()
    time.sleep(5)


def select_departure_date():
    # Select departure date
    cal_departure = driver.find_element(By.XPATH, "//span[text()='Departure']")
    cal_departure.click()
    departure_day = "Sat Dec 13 2025"
    depart_date = driver.find_element(By.XPATH, f"//div[@aria-label='{departure_day}']")
    depart_date.click()
    time.sleep(5)


def select_landing_date():
    # Select landing date
    cal_return = driver.find_element(By.XPATH, "//span[text()='Return']")
    cal_return.click()
    time.sleep(3)
    landing_day = "Thu Jan 01 2026"
    landing_date = driver.find_element(By.XPATH, f"//div[@aria-label='{landing_day}']")
    landing_date.click()
    time.sleep(5)


# Select travellers class
def select_travellers():
    driver.find_element(By.XPATH, "//span[text()='Travellers & Class']").click()
    time.sleep(5)
    age = driver.find_element(By.XPATH, "(//ul[@class='guestCounter font12 darkText gbCounter'])[1]")
    driver.find_element(By.XPATH, "//li[@data-cy='adults-3']").click()
    time.sleep(3)
    # CHOOSE TRAVEL CLASS
    travel_class = driver.find_element(By.XPATH, "//li[text()='Premium Economy']")
    travel_class.click()
    time.sleep(3)


# Apply Button
def apply_button():
    apply_button = driver.find_element(By.XPATH, "//button[@type='button']")
    apply_button.click()
    time.sleep(3)


close_popup()
select_from_city()
select_to_city()
select_departure_date()
select_landing_date()
select_travellers()
apply_button()