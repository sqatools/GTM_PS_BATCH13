
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginPage:
    
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        yield driver
        driver.quit()
    
    def test_valid_login(self, driver):
        # Enter username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("student")
        
        # Enter password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")
        
        # Click login
        login_button = driver.find_element(By.ID, "submit")
        login_button.click()
        
        # Verify success message
        success_msg = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "post-title"))
        )
        assert "Logged In Successfully" in success_msg.text
    
    def test_invalid_password(self, driver):
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("student")
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("WrongPassword")
        
        login_button = driver.find_element(By.ID, "submit")
        login_button.click()
        
        error_msg = driver.find_element(By.ID, "error")
        assert "Invalid" in error_msg.text
