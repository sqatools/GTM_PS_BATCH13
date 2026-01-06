from Rohit.Banking_Project.Page_objects.Banking_website.banking_locator import Delete_Employee_drop_down

website_url = "https://ctcorphyd.com/EBanking_build1/"

# Admin login
Admin_username = "admin"
Admin_Password = "admin"

# Add Branches
Branch_id = "5193"
Branch_Name = "Kolhapur Branch"
Branch_Address = "A/P Shivaji Peth"
Branch_City = "Kolhpaur"
Branch_State = "Maharastra"
Branch_Zipcode = "415125"
Branch_Phone = "9876523678"

ADD_BRANCH_DATA = {
    "branch_id": Branch_id,
    "branch_name": Branch_Name,
    "branch_address": Branch_Address,
    "branch_city": Branch_City,
    "branch_state": Branch_State,
    "branch_zip": Branch_Zipcode,
    "branch_phone": Branch_Phone
}


# update Branch
update_Branch_Name = "Belapur"
update_Branch_Address = "39A CBD Belapur"
update_Branch_City = "Belapur"
update_Branch_State = 'Maharastra'
update_Branch_Zipcode = '415110'
update_Branch_Phone = '6789054021'

# Add New Employee
drop_down_branch = "Yewatmal Branch, 4106"
Employee_ID = "5593"
Employee_FirstName = "Rajkumar"
Employee_LastName = "Sharma"
Employee_Email = "rajkumarsharma@gmail.com"
Employee_Phone = "7389812092"
Employee_Position = "Model Lead"
Employee_HireDate = "05/01/2026"
Employee_Password = "yuio@456"


EMPLOYEE_DB_DATA = {
    "branch_id": drop_down_branch,
    "employee_id":Employee_ID,
    "E_firstname": Employee_FirstName,
    "E_lastname": Employee_LastName,
    "E_email": Employee_Email,
    "E_phone": Employee_Phone,
    "E_position": Employee_Position,
    "E_hire_date": Employee_HireDate,
    "E_password": Employee_Password
}

UPDATE_EMPLOYEE_DATA = {
    "branch_id": 4106,
    "E_firstname": "Mahadev",
    "E_lastname": "Patil",
    "E_email": "mahadevdewkar@gmail.com",
    "E_phone": "5678906542",
    "E_position": "Teacher",
    "E_hire_date": "04/01/2026",
    "E_password": "DFGH@345"
}

# view Employee
view_employee_select_branch = 'Yewatmal Branch, 4106'

# Delete Employees
Delete_Employee_from_drop_down = 'Yewatmal Branch, 4106'

#update Employee
update_employee_branch = 'Yewatmal Branch, 4106'
update_employee_FirstName = 'Sachin'
update_employee_LastName = "Mahadik"
update_employee_Email = "sachinmahadik@gmail.com"
update_employee_Phone = "9097633568"
update_employee_Position = "VP"
update_employee_Hire_date = '05/01/2026'

# Account type
Account_type = 'Demat16 Account'

