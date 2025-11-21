import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver = webdriver.Chrome()
# maximize browser window
driver.maximize_window()
# set implicit timeout
driver.implicitly_wait(10)
# launch url
driver.get("https://www.facebook.com")

# get username field with id="email"
driver.find_element(By.ID, "email").send_keys("user1@gmail.com")
# get password field with id="pass"
driver.find_element(By.ID, "pass").send_keys("user@1234")
# get login button with name="login"
driver.find_element(By.NAME, "login").click()


time.sleep(10)
# close the browser
driver.close()