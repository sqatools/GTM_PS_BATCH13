import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.harmony.bank/online-banking-demo.html")
actions = ActionChains(driver)

login = driver.find_element(By.XPATH,"//a[@href='#oblCollapse']")
login.click()
demo = driver.find_element(By.XPATH,"//a[contains(text(),'Demo')]//parent::li")
demo.click()

def scroll_with_amount():
    time.sleep(5)
    actions.scroll_by_amount(0,500)
    time.sleep(5)

scroll_with_amount()

driver.find_element(By.XPATH,"//a[@class='primary-button' and contains(.,'Personal')]").click()

browser_window = driver.window_handles
print(browser_window)
driver.switch_to.window(browser_window[1])

time.sleep(5)