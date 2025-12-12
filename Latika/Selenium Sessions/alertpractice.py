import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
alert = Alert(driver)


def handle_the_alert():
    driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")

    driver.find_element(By.XPATH,"//button[@onclick='showAlert()']").click()
    time.sleep(5)

    print("Alert text message",alert.text)
    alert.accept()

    driver.find_element(By.XPATH,"//button[@onclick='myDesk()']").click()
    time.sleep(5)
    print(alert.text)
    alert.accept()
    alertmsg=driver.find_element(By.XPATH,"//div[text()='You pressed OK!']")
    print(alertmsg.is_displayed())
    #assert alertmsg == "You pressed OK!"

    driver.find_element(By.XPATH,"//button[@onclick='myPromp()']").click()
    time.sleep(5)
    alert.send_keys("Rahul")
    alert.accept()




handle_the_alert()


