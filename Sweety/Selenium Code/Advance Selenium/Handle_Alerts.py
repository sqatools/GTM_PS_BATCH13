import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
alert = Alert(driver)

def btnShowMsg():
    driver.find_element(By.ID, "btnShowMsg").click()
    time.sleep(5)
    print("alert message", alert.text)
    alert.accept()


#btnShowMsg()

def handle_confirm_alert():
    driver.find_element(By.ID, "button").click()
    time.sleep(5)
    print("alert message", alert.text)
    alert.accept()
    ui_msg = driver.find_element(By.ID, "demo").text
    print("UI message:", ui_msg)
    assert ui_msg == "You pressed OK!"

    driver.find_element(By.ID, "button").click()
    time.sleep(5)
    print("alert message", alert.text)
    alert.dismiss()
    ui_msg = driver.find_element(By.ID, "demo").text
    print("UI message:", ui_msg)
    assert ui_msg == "You pressed Cancel!"


handle_confirm_alert()