import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://sqatools.in/dummy-booking-website/")

elements_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# for element in elements_list:
#     element.click()
#     time.sleep(3)

# select first four
if len(elements_list) >= 4:
    for i in range(0, 4):
        elements_list[i].click()
        time.sleep(3)

# get list of links
links_list = driver.find_elements(By.TAG_NAME, "a")
for elem in links_list:
    print(elem.get_attribute("href"))

driver.close()

