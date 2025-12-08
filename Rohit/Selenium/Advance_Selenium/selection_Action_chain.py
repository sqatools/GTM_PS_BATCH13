import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
action = ActionChains(driver)

def hover_to_the_element():
    menu_item = driver.find_element(By.XPATH,"//div[@id='menu']//a[text()='Tester’s Hub']")
    action.move_to_element(menu_item).perform()
    time.sleep(5)

    sub_menu_item = driver.find_element(By.XPATH,"//div[@id='menu']//span[text()='Demo Testing Site']")
    action.move_to_element(sub_menu_item).perform()
    time.sleep(5)

    sub_menu_item_alert = driver.find_element(By.XPATH,"//div[@id='menu']//span[text()='AlertBox']")
    action.move_to_element(sub_menu_item_alert).click(sub_menu_item_alert).perform()
    time.sleep(5)

#hover_to_the_element()

def drag_drop_element():
    # switch to iframe
    frame_elem = driver.find_element(By.XPATH, "//iframe[contains(@src, 'photo-manager')]")
    driver.switch_to.frame(frame_elem)

    image1 = driver.find_element(By.XPATH, "//h5[text()='High Tatras']//parent::li")
    trash_elem = driver.find_element(By.ID, "trash")

    # perform drag and drop operation
    action.drag_and_drop(image1, trash_elem).perform()
    time.sleep(5)

    for i in range(2, 5):
        image = driver.find_element(By.XPATH, f"//h5[text()='High Tatras {i}']//parent::li")
        trash_elem = driver.find_element(By.ID, "trash")
        # perform drag and drop operation
        action.drag_and_drop(image, trash_elem).perform()
        time.sleep(3)

#drag_drop_element()

def Scroll_to_element_page():
  bottom_elem = driver.find_element(By.XPATH,"//a[text()=' GlobalSQA']")
  action.scroll_to_element(bottom_elem).perform()
  time.sleep(5)
  action.click(bottom_elem).perform()
  time.sleep(5)

#Scroll_to_element_page()

def Scroll_to_with_amount():
    time.sleep(5)
    action.scroll_by_amount(1300,1300).perform()
    time.sleep(5)

#Scroll_to_with_amount()

"""
pip install pyautogui
"""
import pyautogui

def Context_click_or_right_click():  # Right click on website how we are doing inspect
    driver.get("https://automationexercise.com/")
    button_list = driver.find_elements(By.XPATH, "//button[text()='Test Cases']")
    for elem in button_list:
        try:
            action.context_click(elem).perform()
            time.sleep(5)
            pyautogui.press("up")
            time.sleep(5)
            pyautogui.press("enter")
            time.sleep(5)
        except Exception as e:
            print(e)

Context_click_or_right_click()