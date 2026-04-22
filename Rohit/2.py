import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.flipkart.com/")

time.sleep(3)
cancel_btn = driver.find_element(By.XPATH,"//span[contains(@class,'b3wTlE')]").click()
Login_btn = driver.find_element(By.XPATH,"//span[text()='Login']").click()
Enter_Email = driver.find_element(By.XPATH,"//input[contains(@class,'c3Bd2c yXUQVt')]").send_keys("rohitrchavan79@gmail.com")
Enter_OTP = driver.find_element(By.XPATH,"//button[text()='Request OTP']").click()
Enter_Mobile = driver.find_element(By.XPATH,"//input[@class='c3Bd2c yXUQVt']").send_keys("8788980006")
continue_btn = driver.find_element(By.XPATH,"//button[@class='dSM5Ub Kv3ekh KcXDCU']").click()
Request_otp = driver.find_element(By.XPATH,"//button[normalize-space()='Request OTP']").click()
time.sleep(30)
verify_btn = driver.find_element(By.XPATH,"//button[contains(text(),'Verify')]").click()
search_product = driver.find_element (By.XPATH,"((//input[contains(@placeholder,'Search for Products, Brands and More')])[1]").send_keys("samsung 5g mobile")
driver.close()
