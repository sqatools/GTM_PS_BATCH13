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

# Add New Employee
Employee_Menu = (By.XPATH,"//a[normalize-space()='Employees']")
Add_Employee_Submenu = (By.XPATH,"//a[@href='addEmployee.php']")
Drop_Down_Branch = (By.ID,"BranchID")
Employee_id = (By.NAME,"EmployeeID")
Employee_FirstName = (By.NAME,"FirstName")
Employee_LastName = (By.NAME,"LastName")
Employee_Email = (By.NAME,"Email")
Employee_Phone = (By.NAME,"Phone")
Employee_Position = (By.NAME,"Position")
Employee_HireDate = (By.NAME,"HireDate")
Employee_Password = (By.NAME,"Password")
Add_Employee_btn = (By.XPATH,"//input[@value='Add Employee']")
