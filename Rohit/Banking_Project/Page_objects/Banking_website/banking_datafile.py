from Rohit.Banking_Project.Page_objects.Banking_website.banking_locator import Delete_Employee_drop_down

website_url = "https://ctcorphyd.com/EBanking_build1/"

# Admin login
Admin_username = "admin"
Admin_Password = "admin"

# Add Branches
Branch_id = "5124"
Branch_Name = "Chopadi3 Branch"
Branch_Address = "A/P Chopadi2"
Branch_City = "Chopadi2"
Branch_State = "Maharastra"
Branch_Zipcode = "415105"
Branch_Phone = "9876500991"

ADD_BRANCH_DATA = {
    "branch_id": Branch_id,
    "branch_name": Branch_Name,
    "branch_address": Branch_Address,
    "branch_city": Branch_City,
    "branch_state": Branch_State,
    "branch_zip": Branch_Zipcode,
    "branch_phone": Branch_Phone
}

# Add New Employee
drop_down_branch = "Yewatmal Branch, 4106"
Employee_ID = "5520"
Employee_FirstName = "Sudhir"
Employee_LastName = "Kachare"
Employee_Email = "sudhirkachare@gmail.com"
Employee_Phone = "7389812777"
Employee_Position = "M.COM"
Employee_HireDate = "29/12/2025"
Employee_Password = "Karad@123"


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
    "E_firstname": "Promod",
    "E_lastname": "Shewalw",
    "E_email": "promodshewale10@gmail.com",
    "E_phone": "9999999999",
    "E_position": "Senior Tester",
    "E_hire_date": "30/12/2025",
    "E_password": "Admin@123"
}


# Delete Employees
Delete_Employee_from_drop_down = 'Yewatmal Branch, 4106'

