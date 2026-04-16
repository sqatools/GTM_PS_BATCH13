from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.flipkart.com/")

search_product = driver.find_element (By.XPATH,"(//input[contains(@title,'Search for Products, Brands and More')])[1]").send_keys("samsung 5g mobile")
click_on_search_btn = driver.find_element(By.XPATH,'//button[@class="bJtikv"]').click()

driver.close()


