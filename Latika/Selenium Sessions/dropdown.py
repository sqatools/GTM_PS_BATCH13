import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
#driver.get("https://sqatools.in/dummy-booking-website/")

def select_by_Visible_txt_Lbl(label):
    billing_country=driver.find_element(By.ID,"billing_country")
    select_obj=Select(billing_country)
    select_obj.select_by_visible_text(label)
    time.sleep(10)

def select_by_option_value(value):
    billing_country = driver.find_element(By.ID, "billing_country")
    select_obj = Select(billing_country)
    select_obj.select_by_value(value)
    time.sleep(10)

def select_by_index_position(index_value):
    billing_country = driver.find_element(By.ID, "billing_country")
    select_obj = Select(billing_country)
    select_obj.select_by_index(index_value)
    time.sleep(10)

def locate_element_with_Dynamic_dropwown():
    driver.get("https://booking.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    try:
        driver.find_element(By.XPATH, "//button[@aria-label='Dismiss sign-in info.']").click()
    except Exception as e:
        print(e)
    location = driver.find_element(By.XPATH,"//input[@aria-label='Where are you going?']")
    location.click()
    location.send_keys("Pune")
    dropdown_p=driver.find_element(By.XPATH,"//div[@id='autocomplete-results']//ul")
    dropdown_p.find_element(By.XPATH,"//*[text()='Pune']").click()
    time.sleep(5)





#select_by_Visible_txt_Lbl("Algeria")
#select_by_option_value("AS")
#select_by_index_position(2)
locate_element_with_Dynamic_dropwown()
