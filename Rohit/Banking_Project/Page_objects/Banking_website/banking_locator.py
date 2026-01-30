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

# View Branch
click_view_branch_submenu_button = (By.XPATH,"//a[normalize-space()='View Branches']")

# Delete Branch
Delete_Branch_submenu_btn = (By.XPATH,"//a[normalize-space()='Delete Branches']")
Delete_branch = (By.XPATH,"//tr[td[text()='5596']]//img[@src='images/delete.png']")

# update Branch
update_Branch_submenu_btn = (By.XPATH,"//a[normalize-space()='Update Branches']")
update_branch_button = (By.XPATH,"//tr[td[text()='5194']]//img[@src='images/edit.png']")
update_Branch_Name = (By.ID,"BranchName")
update_Branch_Address = (By.ID,"BranchAddress")
update_Branch_City = (By.ID,"BranchCity")
update_Branch_State = (By.ID,"BranchState")
update_Branch_Zipcode = (By.ID,"BranchZipCode")
update_Branch_Phone = (By.ID,"BranchPhone")
update_Branch_update_btn = (By.XPATH,"//input[@value='Update']")


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

# view Employee
view_employee_submenu_btn = (By.XPATH,"//a[normalize-space()='View Employees']")
view_employee_select_branch = (By.ID,"BranchID")
view_employee_view_btn = (By.XPATH,"//input[@value='View']")


# Delete Employees
Delete_Employees_btn = (By.XPATH,"//a[@href='view_del_employee.php']")
Delete_Employee_drop_down = (By.ID,"BranchID")
view_btn = (By.XPATH,"//input[@value='View']")
Delete_Employee_details_btn = (By.XPATH,"//tr[td[text()='5599']]//input[@value='Delete']")

#update Employee
update_employee_btn = (By.XPATH,"//a[normalize-space()='Update Employees']")
update_employee_branch = (By.ID,"BranchID")
update_employee_view_btn = (By.XPATH,"//input[@value='View']")
update_btn= (By.XPATH,"//tr[td[text()='5594']]//input[@type='submit']")
update_employee_FirstName = (By.ID,"FirstName")
update_employee_LastName = (By.ID,"LastName")
update_employee_Email = (By.ID,"Email")
update_employee_Phone = (By.ID,"Phone")
update_employee_Position = (By.ID,"Position")
update_employee_Hire_date = (By.ID,"HireDate")
update_employee_update_btn = (By.XPATH,"//input[@value='Update']")

# Account Types
Account_type_tab = (By.XPATH,"//a[@data-toggle='dropdown' and contains(.,'Account')]")
Add_Account_type_submenu = (By.CSS_SELECTOR,"a[href='addAccountType.php']")
Account_type = (By.NAME,"actype")
Account_type_Add_btn = (By.XPATH,"//input[@value='Add']")


View_Account_type_submenu = (By.CSS_SELECTOR,"a[href='viewAccountTypes.php']")
