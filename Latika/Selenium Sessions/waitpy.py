import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sqatools.in/login-page/")

"""def implicit_wait_practice():

    driver.implicitly_wait(10)
    t1=time.time()

    try:
        driver.find_element(By.ID,"email").send_keys("Abc@gmail.com")
    except Exception as e:
        print(e)
    t2=time.time()
    print("Total time taken :",t2-t1)"""


def explicit_wait():

    wait=WebDriverWait(driver,10)
    t1=time.time()
    try:
        username = wait.until(ec.element_to_be_clickable((By.ID, "email")))
        username.send_keys("user1@gmail.com")
        password=wait.until(ec.element_to_be_clickable((By.XPATH,"//input[@id='pass']")))
        password.send_keys("user@12345")
        loginbtn=wait.until(ec.presence_of_element_located((By.ID,"loginbutton")))
        loginbtn.click()
    except Exception as e:
        print(e)
    t2=time.time()
    print("Total time taken is :",t2-t1)



# implicit_wait_practice()
explicit_wait()
