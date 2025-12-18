from selenium.webdriver.common.by import By

class login_page_locator:
    username_field = (By.NAME, "username")
    password_field = (By.NAME, "password")
    login_button = (By.XPATH, "//button[normalize-space()='Login']")

class admin_page_locator:
    dashboard_heading = (By.XPATH, "//div[@class='oxd-topbar-header-title']//h6")
    admin_side_menu = (By.XPATH, "//span[text()='Admin']//parent::a")
    user_role_dropdown = (By.XPATH, "//label[text()='User Role']//parent::div//parent::div//div[text()='-- Select --']")
    add_user_button = (By.XPATH, "//button[normalize-space()='Add']")
    status_dropdown = (By.XPATH, "//label[text()='Status']//parent::div//parent::div//div[text()='-- Select --']")
    add_user_password_field = (By.XPATH, "//label[text()='Password']//parent::div//parent::div//input")
    add_user_confirm_password = (By.XPATH, "//label[text()='Confirm Password']//parent::div//parent::div//input")
    add_user_username_field = (By.XPATH, "//label[text()='Username']//parent::div//parent::div//input")
    employee_name_field = (By.XPATH, "//label[text()='Employee Name']//parent::div//parent::div//input")
    save_button = (By.XPATH, "//button[normalize-space()='Save']")


