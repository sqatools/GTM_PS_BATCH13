from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://client.schwab.com/Areas/Access/Login")
iframe = driver.find_element(By.ID, "lmsIframe")
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH,"//input[@placeholder='Login ID']").send_keys("maxpars32")
#driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("")
driver.find_element(By.CSS_SELECTOR, "[placeholder^='Pass']").send_keys("Trade4Me@1")
time.sleep(3)
driver.find_element(By.ID,"btnLogin").click()
time.sleep(10)
print("URL: ", driver.current_url)
print("Website Title: ", driver.title)
heading = driver.find_element(By.TAG_NAME, "h1").text
print("Site Heading: ", heading)