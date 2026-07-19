import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.minimize_window()

driver.get("https://testautomationpractice.blogspot.com/")


row = driver.find_element(By.XPATH,"//td[text()='Internet Explorer']//parent::tr")
col = row.find_elements(By.TAG_NAME,"td")

print("CPU:",  col[2].text)
print("Network:", col[3].text)

driver.find_element(By.XPATH,"//button[@id='alertBtn']").click()
simple_alert= driver.switch_to.alert
print(simple_alert.text)
simple_alert.accept()

""""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver,10)
element= wait.until(EC.visibility_of_element_located(By.XPATH,"element"))

driver = webdriver.chrome()
driver.implicitly_Wait(10)
driver.minimize_window()

driver.get("")

login= driver.find_element(By.XPATH,"").send_keys("")
pass = driver.find_element(By.XPATH,"").click()

driver.close()


import pytest

@pytest.fixture(scope="class")

def driver_set(request):
    driver = webdriver.Chrome()
    driver.minimize_window()
    request.cls.driver = driver
    yeild
    driver.close()

"""