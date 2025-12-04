import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://vinothqaacademy.com/alert-and-popup/")
alert = Alert(driver)

def Alert_Box():
    driver.find_element(By.NAME,"alertbox").click()
    time.sleep(10)
    print("Alert Message :", alert.text)
    time.sleep(5)
    alert.accept()
    ui_mgs = driver.find_element(By.XPATH,"//p[@id='demotwo']").text
    print("UI Message :", ui_mgs)
    assert ui_mgs == "You clicked on OK!"

#Alert_Box()

def Confirm_Alert_Box():
    driver.find_element(By.NAME,"confirmalertbox").click()
    print("Alert Message :", alert.text)
    time.sleep(10)
    alert.accept()
    ui_mgs = driver.find_element(By.XPATH,"//p[@id='demo']").text
    print("UI Message :", ui_mgs)
    assert ui_mgs == "You clicked on OK!"

    driver.find_element(By.NAME,"confirmalertbox").click()
    print("Alert Message :", alert.text)
    time.sleep(10)
    alert.dismiss()
    ui_mgs = driver.find_element(By.XPATH,"//p[@id='demo']").text
    print("UI Message :", ui_mgs)
    assert ui_mgs == "You clicked on Cancel!"
    time.sleep(10)

#Confirm_Alert_Box()

def Prompt_Alert_Box():
    driver.find_element(By.XPATH,"//button[@name='promptalertbox1234']").click()
    print("Alert Message :", alert.text)
    time.sleep(10)
    alert.accept()
    time.sleep(5)
    ui_mgs = driver.find_element(By.XPATH,"//p[@id='demoone']").text
    print("UI message :", ui_mgs)
    assert ui_mgs == "Sad to hear it !"

    driver.find_element(By.NAME,"promptalertbox1234").click()
    print("Alert Message :", alert.text)
    time.sleep(10)
    alert.dismiss()
    time.sleep(10)
    ui_mgs = driver.find_element(By.XPATH,"//p[@id='demoone']").text
    print("UI message :", ui_mgs)
    assert ui_mgs == "User cancelled the prompt."

    heading = driver.find_element(By.XPATH,"//h2[text()='Alert and PopUp']")
    print("heading name :", heading.text)

Prompt_Alert_Box()
