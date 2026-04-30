import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as edge_options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Edge()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.naukri.com/")

class Login:
    login_btn = driver.find_element(By.XPATH,"//a[text()='Login']").click()
    username = driver.find_element(By.XPATH,"//input[starts-with(@placeholder,'Enter your active Email ID / Username')]").send_keys("rohitc.career1@gmail.com")
    password = driver.find_element(By.XPATH,"//input[contains(@placeholder,'Enter your password')]").send_keys("SunShine1$RC")
    click_login = driver.find_element(By.XPATH,"//button[text()='Login']").click()
    time.sleep(10)

class upload_Resume:
    view_profile = driver.find_element(By.XPATH,"(//a[@href='/mnjuser/profile'])[1]").click()
    update_resume_btn = driver.find_element(By.XPATH,"//input[@value='Update resume']").click()
    time.sleep(20)
    driver.back()
    time.sleep(15)
driver.close()