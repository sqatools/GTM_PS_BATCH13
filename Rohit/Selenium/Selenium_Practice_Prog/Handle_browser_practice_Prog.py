import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://practicetestautomation.com/practice-test-login/")
action = ActionChains(driver)

driver.find_element(By.XPATH,"//a[text()='Practice']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Test Login Page']").click()

browser_window = driver.window_handles
print(browser_window)
time.sleep(5)
driver.switch_to.window(browser_window[0])

def Scroll_to_with_amount():
    action.scroll_by_amount(400,400).perform()
    time.sleep(5)

Scroll_to_with_amount()

driver.find_element(By.NAME,"username").send_keys("student")
driver.find_element(By.ID,"password").send_keys("Password123")
driver.find_element(By.XPATH,"//button[@id='submit']").click()
time.sleep(10)

driver.find_element(By.XPATH,"//a[text()='Home']").click()

def Scroll_to_element_down():
    scroll_down = driver.find_element(By.XPATH,"//a[text()='privacy policy']")
    action.scroll_to_element(scroll_down).perform()
    time.sleep(10)
    scroll_down.click()
    time.sleep(10)
Scroll_to_element_down()
browser_window = driver.window_handles
print(browser_window)
driver.switch_to.window(browser_window[1])
time.sleep(10)

def Scroll_to_element_bottom():
    scroll_bottom = driver.find_element(By.XPATH,"//a[text()='https://practicetestautomation.com/contact/']")
    action.scroll_to_element(scroll_bottom).perform()
    scroll_bottom.click()
    time.sleep(5)

Scroll_to_element_bottom()

driver.back()
time.sleep(2)
driver.save_screenshot(r"C:\Users\SHREE\OneDrive\Pictures\Screen_shot\Privacy_Policy1.png")

driver.forward()
time.sleep(2)
driver.save_screenshot(r"C:\Users\SHREE\OneDrive\Pictures\Screen_shot\contact_page1.png")

driver.refresh()
time.sleep(2)

heading = driver.find_element(By.XPATH,"//h1[text()='Contact']")
print("heading :", heading.text)


time.sleep(10)
driver.close()
