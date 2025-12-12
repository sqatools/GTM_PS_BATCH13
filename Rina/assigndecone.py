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
    time.sleep(5)

select_by_visible_text_label("India")