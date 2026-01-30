from Rohit.Banking_Project.Page_objects.Banking_website.banking_locator import Delete_Employee_drop_down

website_url = "https://ctcorphyd.com/EBanking_build1/"

# Admin login
Admin_username = "admin"
Admin_Password = "admin"

# Add Branches
Branch_id = "5198"
Branch_Name = "Sajur Branch"
Branch_Address = "A/P Bhavani Peth"
Branch_City = "Thambve"
Branch_State = "Maharastra"
Branch_Zipcode = "415126"
Branch_Phone = "9346523678"

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
update_Branch_Name = "Thambve"
update_Branch_Address = "345S, Koparkarne"
update_Branch_City = "Thambve"
update_Branch_State = 'Maharastra'
update_Branch_Zipcode = '415113'
update_Branch_Phone = '6789054001'

# Add New Employee
drop_down_branch = "Yewatmal Branch, 4106"
Employee_ID = "5599"
Employee_FirstName = "Sambhaji"
Employee_LastName = "Chavan"
Employee_Email = "sambhajichavan23@gmail.com"
Employee_Phone = "7389812762"
Employee_Position = "Automation Engineer"
Employee_HireDate = "06/01/2026"
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
    "E_firstname": "Suraj",
    "E_lastname": "Chavan",
    "E_email": "surajchavan34@gmail.com",
    "E_phone": "5678978542",
    "E_position": "Medical officer",
    "E_hire_date": "06/01/2026",
    "E_password": "DFGH@345"
}

# view Employee
view_employee_select_branch = 'Yewatmal Branch, 4106'

# Delete Employees
Delete_Employee_from_drop_down = 'Yewatmal Branch, 4106'

#update Employee
update_employee_branch = 'Yewatmal Branch, 4106'
update_employee_FirstName = 'Dheeraj'
update_employee_LastName = "Chavan"
update_employee_Email = "dheerajchavan24@gmail.com"
update_employee_Phone = "9097630090"
update_employee_Position = "Project Manager"
update_employee_Hire_date = '06/01/2026'

# Account type
Account_type = 'Demat20 Account'

