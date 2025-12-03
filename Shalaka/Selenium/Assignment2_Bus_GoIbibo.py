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
    time.sleep(5)


# select bus section
def bus_section():
    driver.find_element(By.XPATH, "//span[text()='Bus']").click()
    time.sleep(3)


def enter_source():
    source = driver.find_element(By.XPATH, "//input[@placeholder='Enter Source']")
    source.send_keys("Mumbai")
    driver.find_element(By.XPATH, "// span[text()='Mumbai, Maharashtra']").click()
    time.sleep(3)


def enter_destination():
    destination = driver.find_element(By.XPATH, "//input[@placeholder='Enter Destination']")
    destination.send_keys("Pune")
    driver.find_element(By.XPATH, "// span[text()='Pune, Maharashtra']").click()
    time.sleep(3)


def travel_date():
    date = driver.find_element(By.XPATH, "//input[@placeholder='Pick a date']").click()
    time.sleep(3)
    select_date = driver.find_element(By.XPATH, "//li[span[text()='16']]").click()
    time.sleep(3)


def search_button():
    driver.find_element(By.XPATH, "// button[text()='Search Bus']").click()
    time.sleep(3)


close_popup()
bus_section()
enter_source()
enter_destination()
travel_date()
search_button()

time.sleep(3)


def seat_selection():
    seat = driver.find_element(By.XPATH, "//div[text()='Single Seat']").click()
    time.sleep(2)


def departure_time():
    departure= driver.find_element(By.XPATH, "(//div[text()='6 AM - 12 noon'])[1]").click()
    time.sleep(2)


def arrival_time():
    arrival = driver.find_element(By.XPATH, "(//div[text()='12 noon - 6 PM'])[2]").click()
    time.sleep(2)


seat_selection()
departure_time()
arrival_time()
