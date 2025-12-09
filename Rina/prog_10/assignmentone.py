from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.goibibo.com/")
wait = WebDriverWait(driver, 10)

# close the pop-up
driver.find_element(By.XPATH, "//span[contains(@class, 'logSprite icClose')]").click()
time.sleep(3)

# select option round trip
driver.find_element(By.XPATH, "//li[@data-cy='roundTrip']").click()
time.sleep(5)

# select city from
from_city = driver.find_element(By.ID, "fromCity")
from_city.click()
# click the Box
from_city_input = driver.find_element(By.XPATH, "//input[@placeholder='From']")
# select the name
from_city_input.send_keys("Bangkok")
time.sleep(3)
driver.find_element(By.XPATH, "//p[text()='Bangkok']").click()
print("Bangkok selected")
time.sleep(3)

# select city to
to_city = driver.find_element(By.ID, "toCity")
to_city.click()
driver.find_element(By.XPATH, "//input[@placeholder='To']").send_keys("New Delhi, India")
time.sleep(3)
driver.find_element(By.XPATH, "//p[text()='New Delhi, India']").click()
print("New Delhi selected")
time.sleep(3)

# select departure date
def departure_date():
    # Select departure date
    element = driver.find_element(By.XPATH, "//span[text()='Departure']")
    element.click()
    depart_date = driver.find_element(By.XPATH, f"//div[@aria-label='Sat Dec 20 2025']")
    depart_date.click()
    print("Departure date is Sat Dec 20 2025")
    time.sleep(5)

departure_date()

def arrival_date():
    element = driver.find_element(By.XPATH, "//span[text()='Return']")
    element.click()
    arr_date = driver.find_element(By.XPATH, f"//div[@aria-label = 'Sun Dec 28 2025']")
    arr_date.click()
    print("Return date is Sun Dec 28 2025")
    time.sleep(5)

arrival_date()






# select arrival date
