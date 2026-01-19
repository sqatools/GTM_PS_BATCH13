"""
Implicit wait:  implicit wait is maximum timeout to locate any element,
                -> it applies on all the elements of the webpage.
Explicit wait:  ->  Explicit wait applies on specific element with condition.
                ->  It is maximum to locate the element on the webpage.

Fluent wait: ->  Fluent wait is the polling frequency to locate any element with explicit
                 wait condition.
             ->  Default polling frequency is 0.5 sec.

static wait : ->  it is hard coded sleep time between any specific step. driver has to wait
                  without any condition.
                  e.g. time.sleep(10)
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sqatools.in/login-page/")

def implicit_wait_practice():
    driver.implicitly_wait(10)
    t1 = time.time()
    try:
        driver.find_element(By.ID, "email1").send_keys("user1@gmail.com")
    except Exception as e:
        print(e)
    t2 = time.time()
    print("total time taken :", t2-t1)


# implicit_wait_practice()

def explicit_wait():
    wait = WebDriverWait(driver,  10)

    t1 = time.time()
    try:
        username= wait.until(ec.element_to_be_clickable((By.NAME, "email")))
        username.send_keys("user1@gmail.com")
        # locator should be tuple format
        password = wait.until(ec.presence_of_element_located((By.NAME, "pass1")))
        password.send_keys("User@12345")
    except Exception as e:
        print(e)
    t2 = time.time()
    print("total time taken :", t2-t1)


explicit_wait()










