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

#Orders
Orders_Menu = (By.XPATH,"//a[normalize-space()='Orders']")
Go_Shop_btn = (By.XPATH,"//a[normalize-space()='Go Shop']")
JavaScript_Menu = (By.XPATH,"//a[normalize-space()='JavaScript']")
JS_Data = (By.XPATH,"//h3[text()='JS Data Structures and Algorithm']")
Add_to_Basket = (By.XPATH,"//button[text()='Add to basket']")
View_Basket = (By.XPATH,"//a[text()='View Basket']")
Proceed_to_checkout_btn = (By.XPATH,"//a[normalize-space()='Proceed to Checkout']")

#Shop
shop_Menu = (By.XPATH,"//a[text()='Shop']")
