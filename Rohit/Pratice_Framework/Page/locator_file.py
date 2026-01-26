from selenium.webdriver.common.by import By

create_new_account_btn = (By.XPATH,"//a[text()='Create new account']")
First_Name = (By.XPATH,"//input[@aria-label='First name']")
Surname = (By.NAME,"lastname")
Day = (By.ID,"day")
Month = (By.NAME,"birthday_month")
Year = (By.XPATH,"//select[@aria-label='Year']")
Gender = (By.XPATH,"//label[text()='Male']")
Mobile_number =(By.XPATH,"//input[@aria-label='Mobile number or email address']")
New_Password= (By.XPATH,"//input[@data-type='password']")
Sign_up_btn = (By.XPATH,"//button[@name='websubmit']")