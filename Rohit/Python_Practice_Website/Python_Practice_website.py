import time

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver  = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

class New_User_SignUp:
     driver.get("https://automationexercise.com/login")
     driver.find_element(By.XPATH,"//a[@href='/login']").click()
     driver.find_element(By.NAME,"name").send_keys("Balasaheb More")
     driver.find_element(By.XPATH,"//input[@data-qa='signup-email']").send_keys("dheeraj28@gmail.com")
     time.sleep(10)
     driver.find_element(By.XPATH,"//button[normalize-space()='Signup']").click()

      #Enter Account Information
     driver.find_element(By.ID,"id_gender1").click()
     driver.find_element(By.ID,"password").send_keys("Sajur@123")
     driver.find_element(By.ID,"days").send_keys("13")
     driver.find_element(By.ID,"months").send_keys("January")
     driver.find_element(By.ID,"years").send_keys("2021")
     driver.find_element(By.ID,"optin").click()
     time.sleep(10)
     driver.find_element(By.XPATH,"//input[@data-qa='first_name']").send_keys("Rohit")
     driver.find_element(By.XPATH,"//input[@data-qa='last_name']").send_keys("Chavan")
     driver.find_element(By.XPATH,"//input[@data-qa='company']").send_keys("Infosys")
     driver.find_element(By.XPATH,"//input[@data-qa='address']").send_keys("45A, Earandwana, Kothrud")
     driver.find_element(By.ID,"country").send_keys("India")
     time.sleep(10)
     driver.find_element(By.XPATH,"//input[@data-qa='state']").send_keys("Maharastra")
     driver.find_element(By.XPATH,"//input[@data-qa='city']").send_keys("Karad")
     driver.find_element(By.XPATH,"//input[@data-qa='zipcode']").send_keys("411038")
     driver.find_element(By.XPATH,"//input[@data-qa='mobile_number']").send_keys("9876543200")
     time.sleep(10)
     driver.find_element(By.XPATH,"//button[@data-qa='create-account']").click()
     msg = driver.find_element(
         By.XPATH,
         "//p[contains(normalize-space(),'successfully created')]"
     ).text

     assert "successfully created" in msg

     time.sleep(10)
     driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()
     time.sleep(10)




