from selenium.webdriver.common.by import By

#New_User_Signup
User_Name = (By.XPATH,"//input[@data-qa='signup-name']")
User_Email_address = (By.XPATH,"//input[@data-qa='signup-email']")
User_Signup_btn = (By.XPATH,"//button[@data-qa='signup-button']")

#Enter Account Information:
select_MR = (By.ID,"id_gender1")
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
Logout_btn = (By.XPATH,"//a[normalize-space()='Logout']")

#Login to your account
Login_Email_address= (By.XPATH,"//input[@data-qa='login-email']")
Login_Password = (By.XPATH,"//input[@data-qa='login-password']")
Login_button = (By.XPATH,"//button[@data-qa='login-button']")

#Categary
Men = (By.XPATH,"//a[@href='#Men']")
Tshirt = (By.XPATH,"//a[normalize-space()='Tshirts']")
view_product = (By.XPATH,"//a[@href='/product_details/29']")
Quantity = (By.XPATH,"quantity")
Add_card_button = (By.XPATH,"//button[@class='btn btn-default cart']")
view_cart_button = (By.XPATH,"//a[normalize-space()='View Cart']")
Proceed_to_checkout_btn = (By.XPATH,"//a[normalize-space()='Proceed To Checkout']")
comment_box = (By.XPATH,"//textarea[@name='message']")
Place_order_btn = (By.XPATH,"//a[normalize-space()='Place Order']")
Name_on_card = (By.XPATH,"//input[@data-qa='name-on-card']")
card_number = (By.XPATH,"//input[@data-qa='card-number']")
CVC = (By.XPATH,"//input[@data-qa='cvc']")
Exp_month = (By.XPATH,"//input[@data-qa='expiry-month']")
Exp_year = (By.XPATH,"//input[@data-qa='expiry-year']")
Pay_confirm_btn = (By.XPATH,"//button[@data-qa='pay-button']")
Download_Invoice = (By.XPATH,"//a[normalize-space()='Download Invoice']")
order_continue = (By.XPATH,"//a[@data-qa='continue-button']")

#Women
Polo = (By.XPATH,"//a[@href='/brand_products/Polo']")
Women = (By.XPATH,"//a[normalize-space()='Women']")
Saree = (By.XPATH,"//a[normalize-space()='Saree']")
Saree_view_product = (By.XPATH,"//a[@href='/product_details/41']")
saree_Add_cart = (By.XPATH,"//button[@class='btn btn-default cart']")
saree_view_cart = (By.XPATH,"//a[normalize-space()='View Cart']")
saree_proceed_check_out = (By.XPATH,"//a[normalize-space()='Proceed To Checkout']")
saree_comment_box = (By.XPATH,"//textarea[@name='message']")
Saree_Place_order_btn = (By.XPATH,"//a[normalize-space()='Place Order']")
saree_Name_on_card = (By.XPATH,"//input[@data-qa='name-on-card']")
saree_card_number = (By.XPATH,"//input[@data-qa='card-number']")
saree_CVV = (By.XPATH,"//input[@data-qa='cvc']")
Saree_Exp_Month = (By.XPATH,"//input[@data-qa='expiry-month']")
Saree_Exp_Year = (By.XPATH,"//input[@data-qa='expiry-year']")
Saree_Pay_Confirm_btn = (By.XPATH,"//button[normalize-space()='Pay and Confirm Order']")
Saree_Download_Invoice = (By.XPATH,"//a[normalize-space()='Download Invoice']")
Saree_Continue = (By.XPATH,"//a[normalize-space()='Continue']")


#KIDS
Kids = (By.XPATH,"//a[normalize-space()='Kids']")
Tops_Shirts = (By.XPATH,"//a[normalize-space()='Tops & Shirts']")
click_product = (By.XPATH,"//a[@href='/product_details/13']")
btn_Add_to_cart = (By.XPATH,"//button[normalize-space()='Add to cart']")
click_view_to_Cart = (By.XPATH,"//a[normalize-space()='View Cart']")
click_Proceed_to_checkout = (By.XPATH,"//a[normalize-space()='Proceed To Checkout']")
kid_comments = (By.XPATH,"//textarea[@name='message']")
kids_Place_order = (By.XPATH,"//a[normalize-space()='Place Order']")
Kids_name_of_Card = (By.XPATH,"//input[@data-qa='name-on-card']")
kids_card_no = (By.XPATH,"//input[@data-qa='card-number']")
kids_cvc = (By.XPATH,"//input[@data-qa='cvc']")
kids_Exp_month = (By.XPATH,"//input[@data-qa='expiry-month']")
kids_Exp_Year = (By.XPATH,"//input[@data-qa='expiry-year']")
kids_Pay_Confirm_btn = (By.XPATH,"//button[@data-qa='pay-button']")
kids_downlaod_invoice = (By.XPATH,"//a[normalize-space()='Download Invoice']")
kids_continue_btn = (By.XPATH,"//a[normalize-space()='Continue']")



