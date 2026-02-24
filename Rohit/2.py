import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://career55.sapsf.eu/career?company=wiprolimitP2&loginFlowRequired=true&lang=en_US&_s.crb=xjkSFBytJ0b3RDKaul7gjhvZiezjZHwRW2uegybCKuE%253d")
user_name = driver.find_element(By.XPATH,"//input[starts-with(@id,'username')]").send_keys("rohitchavan0006@gmail.com")
password = driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Samartha@123")
signin_btn = driver.find_element(By.XPATH,"//button[normalize-space()='Sign In']").click()
time.sleep(10)
driver.close()
