import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, wait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://demo.automationtesting.in/Alerts.html")
alert=Alert(driver)
wait=WebDriverWait(driver,10)

def display_alert_box():
    wait.until(ec.element_to_be_clickable((By.XPATH,"//button[@onclick='alertbox()']"))).click()
    alert.accept()
    #print("Alert message is :",alert.text)
    time.sleep(5)

def alert_with_ok_cancel():
    driver.find_element(By.XPATH,"//a[@href='#CancelTab']").click()
    confirm_box=driver.find_element(By.XPATH,"//button[@onclick='confirmbox()']")
    confirm_box.click()
    alert.accept()
    time.sleep(5)
    verify_ok_msg=driver.find_element(By.XPATH,"//p[text()='You pressed Ok']")
    print("Verify alert pop up message",verify_ok_msg.text)
    assert verify_ok_msg.text.strip() == "You pressed Ok"
    # again click for cancel the alert pop up

    confirm_box.click()
    alert.dismiss()
    verify_cancel_msg=driver.find_element(By.XPATH,"//p[text()='You Pressed Cancel']")
    print("Verify alert pop up message with cancel :",verify_cancel_msg.text)
    assert verify_cancel_msg.text.strip() == "You Pressed Cancel"
    time.sleep(5)
def alert_with_prompt():
    driver.find_element(By.XPATH,"//a[@href='#Textbox']").click()
    click_prompt=driver.find_element(By.XPATH,"//button[@onclick='promptbox()']")
    click_prompt.click()

    prompt_msg="Hello Learning alert"
    alert.send_keys("Hello Learning alert")
    alert.accept()
    verify_promt_msg=driver.find_element(By.XPATH,f"//p[contains(text(),'{prompt_msg}')]")
    print("Prompt message:",verify_promt_msg.text)
    assert prompt_msg in verify_promt_msg.text,"Prompt message verification failed."
    time.sleep(5)





display_alert_box()
alert_with_ok_cancel()
alert_with_prompt()

