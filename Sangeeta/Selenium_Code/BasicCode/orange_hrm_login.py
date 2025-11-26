import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# title_header = driver.find_element(By.PARTIAL_LINK_TEXT,"Login")
# print("Header text for the page is :", title_header)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(2)
#driver.find_element(By.CSS_SELECTOR, ".oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
time.sleep(5)
driver.find_element(By.XPATH, "//span[text() = 'Admin']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[@class = 'oxd-topbar-body-nav-tab-item' and contains(text(), 'Job')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[text()='Anhdksss']//parent::div//following-sibling::div//i[@class='oxd-icon bi-pencil-fill']//parent::button").click()
time.sleep(5)

