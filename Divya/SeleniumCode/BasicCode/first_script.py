#Command to install enium# ## pip install selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
def facebook_website():
    driver.get("https://www.facebook.com/")
    driver.find_element(By.ID,"email").send_keys("testemailId@gmail.com")
    driver.find_element(By.NAME, "pass").send_keys("password1")
    # driver.find_element(By.NAME, "login").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()
    time.sleep(10)
    driver.close()

facebook_website()
