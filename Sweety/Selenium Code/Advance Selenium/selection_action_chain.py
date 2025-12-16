import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# //iframe[contains(@src, 'photo-manager')]

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
action = ActionChains(driver)


def hover_to_the_element():
    menu_item = driver.find_element(By.XPATH, "//div[@id='menu']//a[text()='Tester’s Hub']")
    action.move_to_element(menu_item).perform()
    time.sleep(5)
    sub_menu_item = driver.find_element(By.XPATH, "//div[@id='menu']//span[text()='Demo Testing Site']")
    action.move_to_element(sub_menu_item).perform()
    time.sleep(5)

    sub_menu_item_alert = driver.find_element(By.XPATH, "//div[@id='menu']//span[text()='AlertBox']")
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

def scroll_to_element_page():
    bottom_elem = driver.find_element(By.XPATH, "//div[@id='powered']/a[text()=' GlobalSQA']")
    action.scroll_to_element(bottom_elem).perform()
    time.sleep(5)
    action.click(bottom_elem).perform()
    time.sleep(5)


def scroll_to_with_amount():
    time.sleep(5)
    action.scroll_by_amount(500, 500).perform()
    time.sleep(5)

scroll_to_with_amount()