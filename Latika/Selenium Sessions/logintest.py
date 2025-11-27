import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
def open_login_site():
    # Open browser
    #driver = webdriver.Chrome()
    # launch url
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Set implicit timeout
    driver.implicitly_wait(5)
    # Maximize browser window
    driver.maximize_window()
    time.sleep(5)
    # Get the current url
    print("Current URL is :",driver.current_url)

    # Get Website title
    print("Website title is :",driver.title)

    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    # Get Attribute text
    dashboard = driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
    print("Dashboard text is :", dashboard.text)
    time.sleep(5)

def click_admin():
    # Click on Admin tab
    #open_login_site()
    admin=driver.find_element(By.XPATH,"//a[@href='/web/index.php/admin/viewAdminModule']")
    print("Check admin is tab displayed :", admin.is_displayed())
    admin.click()
    print("Admin Page Clicked")
    driver.save_screenshot("Admin_page.png")
    time.sleep(5)

def click_PIM():
    # click on PIM tab
    pim=driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']")
    pim.click()
    print("PIM Page Clicked")
    driver.save_screenshot("PIM_page.png")

def click_Leave():

    leave=driver.find_element(By.XPATH,"//a[@href='/web/index.php/leave/viewLeaveModule']")
    leave.click()
    print("Leave Page Clicked")

    # Enable the Pas Empoyees radio button

    pastemp=driver.find_element(By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
    radiobtn=driver.find_element(By.XPATH,"(//input[@type='checkbox'])[1]")
    print("Verify past emp radio button is selected before :",radiobtn.is_selected())
    print("Is enabled :",radiobtn.is_enabled())
    pastemp.click()
    print("Verify past emp radio button is selected after :",radiobtn.is_selected())
    print("Is enabled :", radiobtn.is_enabled())
    time.sleep(5)


open_login_site()
click_admin()
click_PIM()
click_Leave()






