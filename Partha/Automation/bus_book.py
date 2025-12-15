from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.goibibo.com/bus/")
driver.maximize_window()
#time.sleep(3)
origin = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Enter Source']")))
origin.click()
origin.send_keys("Mumbai")
option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//ul/li//span[text()='Mumbai, Maharashtra']")))
option.click()