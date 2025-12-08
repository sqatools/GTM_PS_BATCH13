import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, wait

driver=webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,10)
driver.get("https://demoqa.com/browser-windows")

def click_new_tab():

    click_tab=driver.find_element(By.ID,"tabButton")
    click_tab.click()

    all_window=driver.window_handles
    print(all_window)

    # switch to new browser tab
    driver.switch_to.window(all_window[1])

    verify_text=wait.until(ec.visibility_of_element_located((By.XPATH,"//h1[text()='This is a sample page']")))
    print("Get the text of new tab :",verify_text.text)

    # switch to back old browser tab
    driver.switch_to.window(all_window[0])

    click_new_window=wait.until(ec.element_to_be_clickable((By.ID,"windowButton")))
    click_new_window.click()
    time.sleep(5)

    driver.current_window_handle
    driver.maximize_window()
    new_win =driver.find_element(By.TAG_NAME,"h1")
    print("get the new window h1 text :",new_win.text)
    time.sleep(10)



click_new_tab()
