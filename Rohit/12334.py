import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/downloads/windows/")
driver.maximize_window()

version = "Python 3.13.14"

# Get all download links under the specified version
links = driver.find_elements(
    By.XPATH,
    f"//a[contains(text(),'{version}')]/ancestor::li/following-sibling::li[1]//a"
)

for link in links:
    print(link.text)

j= input("Enter window installer :")
click_installer = driver.find_element(By.XPATH,"(//a[text()='Windows installer (64-bit)'])[1]").click()

time.sleep(10)


k = input("Enter for Package installer : ")

click_pakage = (By.XPATH,"")