import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://sqatools.in/dummy-booking-website/")

print("Url : ", driver.current_url)
print("Website Title : ", driver.title)
heading = driver.find_element(By.TAG_NAME, ('h1')).text
print(" The header title of webpage is : ", heading)

radio_button = driver.find_element(By.XPATH, "(//input[@type='radio'])[1]")
radio_button.click()
print("Radio button for visa appln ticket is visible :", radio_button.is_displayed())
print("Radio button for visa appln ticket is enabled :", radio_button.is_enabled())
print("Radio button for visa appln ticket is visible :", radio_button.is_selected())
time.sleep(3)

driver.find_element(By.XPATH, "(//input[@type='radio'])[1]").send_keys('Sangs')
driver.find_element(By.XPATH, "").send_keys('Sangs')



