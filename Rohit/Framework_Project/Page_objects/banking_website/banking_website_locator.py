import time

from selenium.webdriver.common.by import By

#Customer_Registration
class RegistrationLoc:
    Customer_Register = (By.XPATH,"//a[@href='register.htm']")
    field_First_Name = (By.NAME,"customer.firstName")
    Last_Name_field = (By.ID,"customer.lastName")
    Address_field = (By.ID,"customer.address.street")
    City_field = (By.ID,"customer.address.city")
    State_field = (By.ID,"customer.address.state")
    Zip_Code_field = (By.NAME,"customer.address.zipCode")
    Phone_field = (By.NAME,"customer.phoneNumber")
    SSN_field = (By.ID,"customer.ssn")
    Username_field = (By.NAME,"customer.username")
    Password_field = (By.ID,"customer.password")
    Confirm_field = (By.ID,"repeatedPassword")
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

class Open_New_Account:
    open_New_Account = (By.XPATH,"//a[@href='openaccount.htm']")
    Account_type = (By.ID,"type")
    ACCOUNT_TYPE_DROPDOWN  = (By.XPATH,"//select[@id='type']")
    FROM_ACCOUNT_DROPDOWN  = (By.ID,"fromAccountId")
    Open_New_Account_btn = (By.XPATH,"//input[@value='Open New Account']")

class Account_Overview:
    account_overview = (By.XPATH,"//a[@href='overview.htm']")

class Funds_Transfer:
    transfer_fund = (By.XPATH,"//a[@href='transfer.htm']")
    Amount = (By.ID,"amount")
    From_account = (By.XPATH,"//select[@id='fromAccountId']")
    To_account = (By.XPATH,"//select[@id='toAccountId']")
    Transfer_btn = (By.XPATH,"//input[@value='Transfer']")

#Bill Payment Service
Bill_Payment_menu= (By.XPATH,"//a[@href='billpay.htm']")
Payee_Name = (By.NAME,"payee.name")
Bill_Address = (By.NAME,"payee.address.street")
Bill_City = (By.NAME,"payee.address.city")
Bill_State = (By.NAME,"payee.address.state")
Bill_Zip_Code = (By.NAME,"payee.address.zipCode")
Bill_Phone = (By.NAME,"payee.phoneNumber")
Bill_Account = (By.NAME,"payee.accountNumber")
Verify_Account = (By.NAME,"verifyAccount")
Bill_Amount = (By.NAME,"amount")
Bill_From_account = (By.NAME,"fromAccountId")
Bill_send_payement = (By.XPATH,"//input[@value='Send Payment']")

#Find Transactions
find_transaction_menu = (By.XPATH,"//a[@href='findtrans.htm']")
Select_an_account = (By.ID,"accountId")
Find_by_Date = (By.ID,"transactionDate")
find_date_btn =(By.ID,"findByDate")
Find_by_from_Date_Range = (By.ID,"fromDate")
Find_by_to_Date_Range = (By.ID,"toDate")
Find_date_Range_btn =(By.ID,"findByDateRange")
Find_by_Amount = (By.ID,"amount")
Find_to_Amount_trans_btn = (By.ID,"findByAmount")

#Update Contact Info
Update_Contact_Info_menu = (By.XPATH,"//a[@href='updateprofile.htm']")
update_First_Name = (By.ID,"customer.firstName")
update_profile_Last_Name = (By.ID,"customer.lastName")
update_profile_Address = (By.ID,"customer.address.street")
update_profile_City = (By.ID,"customer.address.city")
update_profile_State = (By.ID,"customer.address.state")
update_profile_zip_code = (By.ID,"customer.address.zipCode")
update_profile_Phone = (By.ID,"customer.phoneNumber")
update_profile_button = (By.XPATH,"//input[@value='Update Profile']")

#Request_Loan
Request_Loan_Menu = (By.XPATH,"//a[@href='requestloan.htm']")
Requestloan_Loan_Amount = (By.ID,"amount")
Requestloan_Down_Payment = (By.ID,"downPayment")
Requestloan_From_account = (By.ID,"fromAccountId")
Requestloan_Apply_Now_btn = (By.XPATH,"//input[@value='Apply Now']")

#Customer Care
customer_care_menu = (By.XPATH,"//li[@class='contact']/a")
Customer_Care_Name = (By.NAME,"name")
Customer_Care_Email = (By.NAME,"email")
Customer_Care_Phone = (By.NAME,"phone")
Customer_Care_Message = (By.NAME,"message")
Send_to_Customer_Care_btn = (By.XPATH,"//input[@value='Send to Customer Care']")

#ParaSoft Demo Website
ParaSoft_Website_menu = (By.XPATH,"//li[@class='aboutus']/a")

#home_Page
Home_Page_Menu = (By.XPATH,"//li[@class='home']/a")

#ParaBank Is Now Re-Opened
ParaBank_menu = (By.XPATH,"//a[@href='news.htm#6']")

#New! Online Bill Pay
New_Online_bill_Pay = (By.XPATH,"//a[@href='news.htm#5']")

#New! Online Account Transfers
New_online_account_transfer = (By.XPATH,"//a[@href='news.htm#4']")
