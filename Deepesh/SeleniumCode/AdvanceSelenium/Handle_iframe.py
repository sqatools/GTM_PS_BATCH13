import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# //iframe[contains(@src, 'photo-manager')]

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

def switch_To_iframe():
    # switch to iframe
    frame_elem = driver.find_element(By.XPATH, "//iframe[contains(@src, 'photo-manager')]")
    driver.switch_to.frame(frame_elem)

    # get element and click on delete link
    image1 = driver.find_element(By.XPATH, "//h5[text()='High Tatras']//following-sibling::a[@title='Delete this image']")
    image1.click()
    time.sleep(5)

    # get heading text out of the iframe
    # switch to default content
    driver.switch_to.default_content()
    heading = driver.find_element(By.XPATH, "//div[@class='page_heading']/h1")
    print("heading name :", heading.text)

switch_To_iframe()