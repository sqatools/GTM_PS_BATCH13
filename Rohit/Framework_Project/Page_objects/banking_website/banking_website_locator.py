import time

from selenium.webdriver.common.by import By

#Customer_Registration
Customer_Register = (By.XPATH,"//a[@href='register.htm']")
First_Name = (By.ID,"customer.firstName")
Last_Name = (By.ID,"customer.lastName")
Address = (By.ID,"customer.address.street")
City = (By.ID,"customer.address.city")
State = (By.ID,"customer.address.state")
Zip_Code = (By.NAME,"customer.address.zipCode")
Phone = (By.NAME,"customer.phoneNumber")
SSN = (By.ID,"customer.ssn")
Username = (By.NAME,"customer.username")
Password = (By.ID,"customer.password")
Confirm = (By.ID,"repeatedPassword")
Register_btn = (By.XPATH,"//input[@value='Register']")
Logout_btn = (By.XPATH,"//a[@href='logout.htm']")


#Customer_login
CUSTOMER_LOGIN_USERNAME = (By.NAME,"username")
CUSTOMER_LOGIN_PASSWORD = (By.NAME,"password")
LOGIN_BUTTON = (By.XPATH,"//input[@value='Log In']")
LOGOUT_BUTTON= (By.XPATH,"//a[@href='logout.htm']")

#customer_forgot_login
forgot_login_btn = (By.XPATH,"//a[@href='lookup.htm']")
forgot_login_FirstName = (By.ID,"firstName")
forgot_login_LastName = (By.ID,"lastName")
forgot_login_Address = (By.ID,"address.street")
forgot_login_City = (By.ID,"address.city")
forgot_login_State = (By.ID,"address.state")
forgot_login_Zip_Code = (By.NAME,"address.zipCode")
forgot_login_SSN = (By.ID,"ssn")
find_my_login_info_btn = (By.XPATH,"//input[@value='Find My Login Info']")

#Open_New_Account
Open_New_Account = (By.XPATH,"//a[@href='openaccount.htm']")
Account_type = (By.ID,"type")
ACCOUNT_TYPE_DROPDOWN  = (By.XPATH,"//option[text()='SAVINGS']")
from_account = (By.ID,"fromAccountId")
FROM_ACCOUNT_DROPDOWN  = (By.XPATH,"//option[@value='23889']")
Open_New_Account_btn = (By.XPATH,"//input[@value='Open New Account']")