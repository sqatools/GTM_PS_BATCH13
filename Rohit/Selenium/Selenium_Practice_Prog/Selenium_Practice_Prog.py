import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

'''
def Test_login():
    driver.get("https://practicetestautomation.com/practice-test-login/")
    heading = driver.find_element(By.TAG_NAME,"h2" )
    print("Print Heading :",heading.text)
    driver.find_element(By.ID,"username" ).send_keys("student")
    driver.find_element(By.NAME,"password").send_keys("Password123")
    driver.find_element(By.ID,"submit").click()
    driver.find_element(By.ID,"menu-item-21").click()
    driver.find_element(By.ID,"menu-item-18").click()
    driver.find_element(By.ID,"wpforms-161-field_0").send_keys("Rohit")
    driver.find_element(By.ID,"wpforms-161-field_0-last").send_keys("Chavan")
    driver.find_element(By.ID,"wpforms-161-field_1").send_keys("dheeraj0006@gmail.com")
    driver.find_element(By.NAME,"wpforms[fields][2]").send_keys("Learning Python Program")
    driver.find_element(By.ID,"wpforms-submit-161").click()
    time.sleep(10)
    driver.close()

Test_login()
'''

def Booking():
    driver.get("https://www.booking.com/")
    heading = driver.find_element(By.TAG_NAME, "h2")
    print("Print Heading :", heading.text)
    driver.find_element(By.ID,'packages').click()


    time.sleep(10)
    driver.close()
Booking()

