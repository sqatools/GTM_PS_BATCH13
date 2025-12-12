
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/dummy-booking-website/")

def select_by_visible_text_label(label):
    dropdown = driver.find_element(By.ID, "billing_country")
    select_obj = Select(dropdown)
    select_obj.select_by_visible_text(label)
    time.sleep(10)

#select_by_visible_text_label("American Samoa")

def select_by_option_value(option_value):
    dropdown = driver.find_element(By.ID, "billing_country")
    select_obj = Select(dropdown)
    select_obj.select_by_value(option_value)
    time.sleep(10)

#select_by_option_value("AG")

def select_by_index_position(index_value):
    dropdown = driver.find_element(By.ID, "billing_country")
    select_obj = Select(dropdown)
    select_obj.select_by_index(index_value)
    time.sleep(10)

#select_by_index_position(1)

def locate_element_with_dynamic_dropdown():
    driver.get("https://www.booking.com")
    driver.maximize_window()
    time.sleep(10)
    input_field = driver.find_element(By.XPATH, "//input[@placeholder='Where are you going?']")
    input_field.click()
    input_field.send_keys("Pune")
    time.sleep(5)
    # find element with child traversing concept.
    dpwn_parent = driver.find_element(By.XPATH, "//div[@id='autocomplete-results']//ul")
    dpwn_parent.find_element(By.XPATH, "//*[text()='Pune']").click()
    time.sleep(10)



locate_element_with_dynamic_dropdown()