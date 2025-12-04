from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.goibibo.com/")

driver.find_element(By.XPATH, "//span[@class='logSprite icClose']").click()
time.sleep(5)
try:
    ad_elem = driver.find_element(By.XPATH, "//div[contains(@data-id, 'pip_id')]/p")
    ad_elem.click()
except Exception as e :
    pass

driver.find_element(By.XPATH, "//li[@data-cy='roundTrip']").click()
time.sleep(2)
input_field = driver.find_element(By.XPATH, "//input[@id='fromCity']")
input_field.click()


dest_from = driver.find_element(By.XPATH, "//input[@placeholder='From']")
dest_from.send_keys('Hyderabad')
time.sleep(2)
driver.find_element(By.XPATH, "//span[text() = 'Hyderabad']//ancestor::li").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='toCity']").click()
dest_to = driver.find_element(By.XPATH, "//input[@placeholder='To']")
dest_to.send_keys('Navi Mumbai')
driver.find_element(By.XPATH, "//span[text() = 'Navi Mumbai']//ancestor::li").click()

time.sleep(2)
driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Dec 10 2025')]").click()
driver.find_element(By.XPATH, "(//p[text() = '6']//parent::div)[1]").click()
time.sleep(2)
#driver.find_element(By.XPATH, "(//div[@aria-label = 'Sat Jan 03 2026'])[2]").click()
#driver.find_element(By.XPATH, "//span[@aria-label = 'Next Month']").click()
driver.find_element(By.XPATH, "//span[@data-cy ='travellerText']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[@data-cy ='adults-2']").click()
driver.find_element(By.XPATH, "//li[@data-cy ='travelClass-0']").click()




