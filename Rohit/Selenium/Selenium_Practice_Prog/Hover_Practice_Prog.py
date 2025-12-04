import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
action = ActionChains(driver)

def hovering():
   menu = driver.find_element(By.XPATH,"//li[@id='menu-item-2822']")
   action.move_to_element(menu).perform()
   time.sleep(5)

   sub_menu = driver.find_element(By.XPATH,"//li[@id='menu-item-2824']")
   action.move_to_element(sub_menu).perform()
   time.sleep(5)

   sub_sub_menu = driver.find_element(By.XPATH,"//div[@id='menu']//span[text()='Registration Form']")
   action.move_to_element(sub_sub_menu).click().perform()
   time.sleep(10)

hovering()