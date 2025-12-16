from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def rgt_click(driver):
    driver.get("http://automationexercise.com")
    buttonlist = driver.find_elements(By.XPATH, "//button[text()='Test Cases']")
    for button in buttonlist:
        try:
            action.context_click(button).perform()
        except Exception as e:
            print(e)
rgt_click()