import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")

Name = driver.find_element(By.XPATH,"//input[@placeholder='Enter Name']").send_keys("Rohit")
Email = driver.find_element(By.XPATH,"//input[contains(@id,'email')]").send_keys("rohitchavan@gmail.com")

select = Select(driver.find_element(By.ID,"country"))
select.select_by_visible_text("Australia")
time.sleep(10)

row = driver.find_element(By.XPATH,"//td[text()='Chrome']//parent::tr")
coln = row.find_elements(By.XPATH,"td")

print("Memory :",coln[3].text)
time.sleep(10)
driver.close()

