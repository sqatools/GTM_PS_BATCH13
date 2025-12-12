import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
alert = Alert(driver)

def Alert_Message():
    driver.find_element(By.ID,"btnShowMsg").click()
    time.sleep(5)
    print("Alert Message", alert.text)
    alert.accept()

#Alert_Message()

def Confirm_Box():
    driver.find_element(By.ID,"button").click()
    time.sleep(5)
    print("Alert Message", alert.text)
    alert.accept()
    ui_msg = driver.find_element(By.ID, "demo").text
    print("UI message:", ui_msg)
    assert ui_msg == "You pressed OK!"

    driver.find_element(By.ID, "button").click()
    time.sleep(5)
    print("Alert Message", alert.text)
    alert.dismiss()
    ui_msg = driver.find_element(By.ID, "demo").text
    print("UI message:", ui_msg)
    assert ui_msg == "You pressed Cancel!"
    time.sleep(5)
#Confirm_Box()

def Prompt_Box():
    driver.find_element(By.ID,"promptbtn").click()
    time.sleep(5)
    print("Alert Message", alert.text)
    alert.accept()
    ui_msg = driver.find_element(By.ID, "prompt").text
    print("UI message:", ui_msg)
    assert ui_msg == "Hello Harry Potter! How are you today?"
    time.sleep(5)

    driver.find_element(By.ID, "promptbtn").click()
    time.sleep(5)
    print("Alert Message", alert.text)
    alert.dismiss()
    ui_msg = driver.find_element(By.ID, "prompt").text
    print("UI message:", ui_msg)
    assert ui_msg == "User cancelled the prompt."
    time.sleep(5)

Prompt_Box()