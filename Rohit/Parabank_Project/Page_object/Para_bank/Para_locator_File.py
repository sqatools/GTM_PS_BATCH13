from selenium.webdriver.common.by import By

#Register
Register_menu = (By.XPATH,"//a[text()='Register']")
First_Name = (By.XPATH,"//input[contains(@id,'customer.firstName')]")
Last_Name = (By.XPATH,"//input[contains(@name,'customer.lastName')]")
Address = (By.XPATH,"//input[contains(@id,'customer.address.street')]")
City = (By.XPATH,"//input[contains(@id,'customer.address.city')]")
State = (By.XPATH,"//input[contains(@id,'customer.address.state')]")
Zip_code = (By.XPATH,"//input[contains(@id,'customer.address.zipCode')]")
Phone = (By.XPATH,"//input[contains(@id,'customer.phoneNumber')]")
SSN = (By.XPATH,"//input[contains(@id,'customer.ssn')]")
Username = (By.XPATH,"//input[contains(@id,'customer.username')]")
Password = (By.XPATH,"//input[contains(@id,'customer.password')]")
Confirm = (By.XPATH,"//input[contains(@id,'repeatedPassword')]")
Register_btn = (By.XPATH,"//input[contains(@value,'Register')]")

#Customer Login
User_name = (By.XPATH,"//input[starts-with(@name,'username')]")
password = (By.XPATH,"//input[starts-with(@name,'password')]")
Login_btn = (By.XPATH,"//input[starts-with(@value,'Log In')]")