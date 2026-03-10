# LLM Utilities
# Helper functions for LLM interactions
from openai import OpenAI
from config import API_KEY, TEST_MODE


def get_mock_response(prompt):
    """Generate realistic mock responses for testing without API key"""
    
    if "Analyze the requirement" in prompt or "extract" in prompt:
        return """
Feature: Login Functionality Testing

Test Scenarios:
1. Valid User Login
   - User enters valid username and password
   - Expected: User successfully logs in and redirected to dashboard
   
2. Invalid Username
   - User enters invalid username
   - Expected: Error message displayed, user remains on login page
   
3. Invalid Password
   - User enters valid username but wrong password
   - Expected: Error message displayed, user remains on login page
   
4. Empty Fields
   - User leaves username or password empty
   - Expected: Validation error message displayed
   
5. Case Sensitivity
   - Test if username/password are case-sensitive
   - Expected: Should handle appropriately based on requirement
"""
    
    elif "Create detailed test cases" in prompt:
        return """
TEST CASE 1: Valid User Login
- Precondition: User is on login page
- Steps:
  1. Enter username: student
  2. Enter password: Password123
  3. Click Login button
- Expected Result: Success message displayed, redirected to dashboard

TEST CASE 2: Invalid Password
- Precondition: User is on login page
- Steps:
  1. Enter username: student
  2. Enter password: WrongPassword
  3. Click Login button
- Expected Result: Error message "Invalid credentials" displayed

TEST CASE 3: Empty Username
- Precondition: User is on login page
- Steps:
  1. Leave username empty
  2. Enter password: Password123
  3. Click Login button
- Expected Result: Validation error "Username required" displayed

TEST CASE 4: SQL Injection
- Precondition: User is on login page
- Steps:
  1. Enter username: admin' OR '1'='1
  2. Enter password: anything
  3. Click Login button
- Expected Result: Login rejected, no database access
"""
    
    elif "Write Selenium pytest automation script" in prompt:
        return """
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
"""
    
    else:
        return "Mock response for: " + prompt[:100]


def ask_llm(prompt):
    """Call OpenAI API or return mock response in test mode"""
    
    if TEST_MODE:
        print("[TEST MODE] Using mock LLM response...")
        return get_mock_response(prompt)
    
    # Real API call
    client = OpenAI(api_key=API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content
