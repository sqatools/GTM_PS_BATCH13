from selenium.webdriver.common.by import By

First_name = (By.XPATH,"//input[@placeholder='First Name']")
Last_name = (By.XPATH,"//input[@placeholder='Last Name']")
Address = (By.XPATH,"//textarea[@ng-model='Adress']")
Email_address = (By.XPATH,"//input[@type='email']")
Phone = (By.XPATH,"//input[@ng-model='Phone']")
male_radio_btn = (By.XPATH,"//input[@type='radio' and @value='Male']")
Cricket_check_box = (By.ID,"checkbox1")
Language_dropdown = (By.XPATH,"//div[@id='msdd']")
Language_options = (By.XPATH,"//ul[contains(@class,'ui-autocomplete')]//li/a")
Skills_dropdown = (By.ID,"Skills")
Skills_options = (By.XPATH,"//option[@value='Linux']")

