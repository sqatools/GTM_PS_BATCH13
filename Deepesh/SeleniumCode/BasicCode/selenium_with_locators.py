"""
List locators:
1). ID
2). NAME
3). LINK TEXT
4). PARTIAL LINK TEXT
5). CLASS
6). TAGNAME
7). CSS_SELECTOR
8). XPATH

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver = webdriver.Chrome()
# maximize browser window
driver.maximize_window()
# set implicit timeout
driver.implicitly_wait(10)

def facebook_website():
    # launch url
    driver.get("https://www.facebook.com")

    # get element with tagname and print the heading of facebook
    heading = driver.find_element(By.TAG_NAME, "h2")
    print(heading)
    print("facebook heading :", heading.text)

    # get username field with id="email"
    # driver.find_element(By.ID, "email").send_keys("user1@gmail.com")
    user_field = driver.find_element(By.ID, "email")
    user_field.send_keys("user1@gmail.com")

    # get password field with NAME locator
    driver.find_element(By.NAME, "pass").send_keys("user@1234")

    # get login button with name="login"
    # driver.find_element(By.NAME, "login").click()

    # get element with link text
    # driver.find_element(By.LINK_TEXT, "Forgotten password?").click()

    # get element with partial link text
    driver.find_element(By.PARTIAL_LINK_TEXT, "Forgotten").click()

    time.sleep(10)
    # close the browser
    driver.close()

facebook_website()

# Homework to automate the login website
# https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# https://sqatools.in/python-selenium-installation/