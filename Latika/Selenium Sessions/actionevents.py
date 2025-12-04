import time
from argparse import Action

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://vinothqaacademy.com/mouse-event/")
wait=WebDriverWait(driver,10)
action=ActionChains(driver)

def drag_n_drop():

    source=driver.find_element(By.ID,"draggableElement")
    dest=driver.find_element(By.ID,"droppableElement")
    try:
        action.drag_and_drop(source,dest).perform()
        print("Drag and drop performed")
    except Exception as e:
        print(e)
    time.sleep(10)

def double_click():

    dbl_click=wait.until(ec.element_to_be_clickable((By.ID,"dblclick")))
    action.double_click(dbl_click).perform()

    verify_msg=wait.until(ec.visibility_of_element_located((By.XPATH,"//p[text()='Double Click Action is Performed']")))
    print(verify_msg.text,"Message after double clicked")
    time.sleep(5)

def right_click():
    right_click=wait.until(ec.element_to_be_clickable((By.ID,"rightclick")))
    action.context_click(right_click).perform()

    click_menu=wait.until(ec.element_to_be_clickable((By.XPATH,"(//a[@href='https://vinothqaacademy.com/mouse-event/'])[3]")))
    action.click().perform()
    time.sleep(5)


drag_n_drop()
double_click()
