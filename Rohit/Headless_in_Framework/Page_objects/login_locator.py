from selenium.webdriver.common.by import By

Username = (By.ID,"username")
Password = (By.ID,"password")
login_Submit = (By.ID,"submit")
contact_tab = (By.XPATH, "//a[normalize-space()='Contact']")
First_name = (By.XPATH,"//input[@id='wpforms-161-field_0']")
Last_name = (By.XPATH,"//input[@id='wpforms-161-field_0-last']")
Email = (By.ID,"wpforms-161-field_1")
Message = (By.XPATH,"//textarea[@id='wpforms-161-field_2']")
Contact_Submit = (By.XPATH,"//button[@id='wpforms-submit-161']")

