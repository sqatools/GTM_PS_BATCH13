import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver=webdriver.Chrome()
driver.maximize_window()

wait=WebDriverWait(driver,10)
driver.get("https://demo.automationtesting.in/Frames.html")

def handle_iframe():

    single_iframe=wait.until(ec.visibility_of_element_located((By.ID,"singleframe")))
    driver.switch_to.frame(single_iframe)
    wait.until(ec.visibility_of_element_located((By.XPATH,"(//input[@type='text'])[1]"))).send_keys("Hello")
    time.sleep(10)
    driver.switch_to.default_content()

def handle_multiple_iframe():

    click_multiple_iframe=wait.until(ec.element_to_be_clickable((By.XPATH,"//a[@href='#Multiple']")))
    click_multiple_iframe.click()
    time.sleep(10)
    nested_iframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
    driver.switch_to.frame(nested_iframe)



handle_iframe()
handle_multiple_iframe()

