with open ("2ndFiles.txt","r") as f:
    line = f.read()
    print(len(line))

with open("2ndFiles.txt","w") as f:
    f.write("Hy guys Good Morning")


with open ("2ndFiles.txt","a") as f:
    f.write("Hy Good Night")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

row = driver.find_element(By.XPATH,"//td[normalize-space()='Internet Explorer']/parent::tr")

cols = row.find_elements(By.TAG_NAME,"td")

print("CPU:",cols[2].text)


