from selenium.webdriver.common.by import By

#New_User_Signup
User_Name = (By.XPATH,"//input[@data-qa='signup-name']")
User_Email_address = (By.XPATH,"//input[@data-qa='signup-email']")
User_Signup_btn = (By.XPATH,"//button[@data-qa='signup-button']")

#Enter Account Information:
select_MR = (By.XPATH,"//input[@value='Mr']")
Password = (By.XPATH,"//input[@data-qa='password']")
Date = (By.XPATH,"//select[@data-qa='days']")
Month = (By.XPATH,"//select[@data-qa='months']")
Year = (By.XPATH,"//select[@data-qa='years']")
specail_offer_checkbox = (By.ID,"optin")

#Address Information
First_Name = (By.XPATH,"//input[@data-qa='first_name']")
Last_Name = (By.XPATH,"//input[@data-qa='last_name']")
Company = (By.XPATH,"//input[@data-qa='company']")
Address = (By.XPATH,"//input[@data-qa='address']")
Country = (By.XPATH,"//input[@data-qa='country']")
State = (By.XPATH,"//input[@data-qa='state']")
City = (By.XPATH,"//input[@data-qa='city']")
Zipcode = (By.XPATH,"//input[@data-qa='zipcode']")
Mobile_number = (By.XPATH,"//input[@data-qa='mobile_number']")
Create_Account_btn = (By.XPATH,"//button[normalize-space()='Create Account']")
continue_btn = (By.XPATH,"//a[@data-qa='continue-button']")


