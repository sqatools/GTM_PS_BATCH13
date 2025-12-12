import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)


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
    time.sleep(5)
    #checkbox = driver.find_element(By.CSS_SELECTOR, "[class='recaptcha-checkbox-checkmark']")
    #checkbox.click()
    #checkbox = driver.find_element(By.ID, "recaptcha-anchor")
    #checkbox.click()
    driver.find_element(By.ID,"wpforms-submit-161").click()
    time.sleep(10)
    driver.close()

Test_login()


######################################################################################
'''
driver.get("https://automationexercise.com/login")
time.sleep(5)
driver.find_element(By.NAME,"name").send_keys("Rohit Chavan")
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("rohitrchavan09@gmail.com")
driver.find_element(By.XPATH,"//button[@data-qa='signup-button']").click()
driver.find_element(By.ID,'id_gender1').click()
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Karad@123")
day_dropdown = driver.find_element(By.ID,"days")
select_day = Select(day_dropdown)
select_day.select_by_index(2)
print("select days :", select_day.first_selected_option.text)

month_dropdown = driver.find_element(By.NAME,"months")
select_month = Select(month_dropdown)
select_month.select_by_visible_text("December")

select_year = driver.find_element(By.NAME, "years")
select_year.send_keys('1992')

driver.find_element(By.NAME,"newsletter").click()
driver.find_element(By.ID, "first_name").send_keys("Rohit")
driver.find_element(By.ID, "last_name").send_keys("Chavan")
driver.find_element(By.NAME, "company").send_keys("TCS")
driver.find_element(By.ID, "address1").send_keys('Karad')
driver.find_element(By.NAME, "address2").send_keys('Maharastra')

country_dropdown = driver.find_element(By.NAME,"country")
select_year = Select(country_dropdown)
select_year.select_by_visible_text("United States")

driver.find_element(By.XPATH, "//input[@id='state']").send_keys("Maharastra")
driver.find_element(By.XPATH, "//input[@name='city']").send_keys("Pune")
driver.find_element(By.ID,"zipcode").send_keys('415110')
driver.find_element(By.XPATH, "//input[@name='mobile_number']").send_keys('8745635735')
driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()
driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()
driver.find_element(By.XPATH, "//a[@href='/logout']").click()


time.sleep(10)
driver.close()

'''


