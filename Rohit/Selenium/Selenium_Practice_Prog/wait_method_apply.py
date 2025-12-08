import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver =  webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationexercise.com/login")

def implicit_wait_practice():
    driver.implicitly_wait(5)
    t1 = time.time()
    try:
        login_user = driver.find_element(By.NAME,"email1")
        login_user.send_keys("user12@gmail.com")

    except Exception as e:
        print(e)
    t2 = time.time()
    print("Total time taken :", t2-t1)

#implicit_wait_practice()

def explicit_wait():
    wait = WebDriverWait(driver,10)
    t1 = time.time()
    try:
        login_password = wait.until(EC.element_to_be_clickable((By.NAME,"password1")))
        login_password.send_keys("Karad@123")
    except Exception as e:
        print(e)
    t2 = time.time()
    print("Total time taken to password :", t2-t1)

explicit_wait()

login_button = driver.find_element(By.XPATH,"//button[@data-qa='login-button']")
login_button.click()

time.sleep(10)
