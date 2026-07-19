import time
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.gtpcm.ford.com/Home")
action = ActionChains(driver)

def hovering():
    data_Exchange = driver.find_element(By.XPATH,"(//li[@role='menuitem'])[1]")
    action.move_to_element(data_Exchange).click().perform()
    time.sleep(50)

    Connect_request = driver.find_element(By.XPATH,"(//li[@role='menuitem'])[2]")
    action.move_to_element(Connect_request).perform()
    time.sleep(50)

hovering()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.gtpcm.ford.com/Home")

wait = WebDriverWait(driver, 20)


def hovering():

    # First menu
    data_exchange = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "(//li[@role='menuitem'])[1]")
        )
    )

    ActionChains(driver)\
        .move_to_element(data_exchange)\
        .click()\
        .perform()

    time.sleep(2)

    # Second menu after first opens
    connect_request = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "(//li[@role='menuitem'])[2]")
        )
    )

    ActionChains(driver)\
        .move_to_element(connect_request)\
        .perform()

    time.sleep(5)


hovering()

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://sqatools.in/dummy-booking-website/")

# Find all checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# Select one by one
for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()
        time.sleep(1)    # Optional: wait for 1 second to see the selection

driver.quit()

