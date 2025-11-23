import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def open_login_site():
    # Open browser
    driver = webdriver.Chrome()
    # launch url
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Set implicit timeout
    driver.implicitly_wait(10)
    # Maximize browser window
    driver.maximize_window()
    time.sleep(10)

    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(10)

open_login_site()






