from selenium.webdriver.common.by import By

My_Account = (By.XPATH,"//a[normalize-space()='My Account']")

#Registration
Email_Address = (By.XPATH,"//input[starts-with(@id,'reg_email')]")
Password_btn = (By.XPATH,"//input[contains(@id,'reg_password')]")
Register_btn = (By.XPATH,"//input[@value='Register']")
Sign_out_btn = (By.XPATH,"//a[normalize-space()='Sign out']")

#Login
Login_Username = (By.XPATH,"//input[contains(@id,'username')]")
Login_Psd = (By.XPATH,"//label[normalize-space()='Password *']/following::input[@id='password']")
Login_btn = (By.XPATH,"//input[@value='Login']")
Logout_btn = (By.XPATH,"//a[normalize-space()='Logout']")
