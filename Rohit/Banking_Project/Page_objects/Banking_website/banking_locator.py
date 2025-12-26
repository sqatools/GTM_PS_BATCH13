from selenium.webdriver.common.by import By

#Admin login
Admin_menu = (By.XPATH,"//a[@href='admin.php']")
Admin_username = (By.XPATH,"//input[@placeholder='Enter Username']")
Admin_Password = (By.XPATH,"//input[@placeholder='Enter Password']")
Admin_login = (By.XPATH,"//input[@value='Login']")
Admin_Reset = (By.XPATH,"//input[@value='Reset']")

# Add Branches
Branch_tab = (By.XPATH,"//a[normalize-space()='Branches']")
Add_Branches_Submenu = (By.XPATH,"//a[@href='branches.php']")
Branch_id = (By.ID,"BranchID")
Branch_Name = (By.ID,"BranchName")
Branch_Address = (By.ID,"BranchAddress")
Branch_City = (By.ID,"BranchCity")
Branch_State = (By.ID,"BranchState")
Branch_Zipcode = (By.ID,"BranchZipCode")
Branch_Phone = (By.ID,"BranchPhone")
Add_Branch_btn = (By.XPATH,"//input[@value='Add Branch']")
Branch_Reset_btn = (By.XPATH,"//input[@value='Reset']")

