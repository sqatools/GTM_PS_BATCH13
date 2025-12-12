import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://sqatools.in/dummy-booking-website/")
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Login Page").click()
time.sleep(5)

browser_winds = driver.window_handles
print(browser_winds)
# switch to new browser tab, it will be in 1 position on window list
driver.switch_to.window(browser_winds[1])

# interact with element on new tab
driver.find_element(By.ID, "email").send_keys("user1@gmail.com")
driver.find_element(By.ID, "pass").send_keys("user@12345")
time.sleep(5)
driver.find_element(By.ID, "loginbutton").click()

# switch to original tab
driver.switch_to.window(browser_winds[0])
heading = driver.find_element(By.TAG_NAME, "h1")
print("heading :", heading.text)

time.sleep(5)

driver.close()


