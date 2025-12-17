from selenium.webdriver.common.by import By

radio_button = driver.find_element(By.XPATH, "(//input[@type='radio'])[1]")
first_name = (By.NAME, "firstname")
dob_calender = (By.ID, "birthday")
male_radio_btn = (By.ID, "male")
travellers_dropdown = (By.ID, "admorepass")

from_city_field = (By.NAME, "fromcity")
dest_city_field = (By.NAME, "destcity")
billing_name_field = (By.ID, "billing_name")
billing_phone_field = (By.ID, "billing_phone")