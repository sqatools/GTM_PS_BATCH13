from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
action = ActionChains(driver)

def Menu_hover():
    menu = driver.find_element(By.XPATH,"(//a[text()='Tester’s Hub'])[1]")
    action.move_to_element(menu).perform()

