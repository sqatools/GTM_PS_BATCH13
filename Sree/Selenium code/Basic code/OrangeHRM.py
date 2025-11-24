import time

from selenium import webdriver
from selenium.webdriver.common.by import By

dr=webdriver.Chrome()
dr.maximize_window()
dr.implicitly_wait(10)
dr.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
dr.find_element(By.NAME,"username").send_keys("Admin")
dr.find_element(By.NAME,"password").send_keys("admin123")
dr.find_element(By.," oxd-button oxd-button--medium oxd-button--main orangehrm-login-button ").click()