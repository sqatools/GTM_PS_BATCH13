import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

Name =driver.find_element(By.XPATH,"//input[@placeholder='Enter Name']").send_keys("Rohit Chavan")
Email =driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter EMail']").send_keys("dheerajchahavn@gmail.com")
Phone = driver.find_element(By.XPATH,"//input[@placeholder='Enter Phone']").send_keys("8765432909")
Address =driver.find_element (By.XPATH,"//textarea[@id='textarea']").send_keys("456Q, Dyneshar Apartment, Near Supar Market, Karad")
Gender = driver.find_element(By.ID,"male").click()
Country = driver.find_element(By.ID,"country").click()
dp_value = driver.find_element(By.XPATH,"//option[@value='australia']").click()
Color = driver.find_element(By.XPATH,"//option[@value='white']").click()
sorted_filter = driver.find_element(By.XPATH,"//option[@value='elephant']").click()
Date_Picker1 = driver.find_element(By.ID,'datepicker').send_keys("02/10/2026")
Date_Picker2 = driver.find_element(By.XPATH,"//input[@id='txtDate']").send_keys("02/02/2026")
Date_Picker3_Start_date = driver.find_element(By.XPATH,"//input[@placeholder='Start Date']").send_keys("15/02/2026")
Date_Picker3_End_date = driver.find_element(By.XPATH,"//input[@placeholder='End Date']").send_keys("25/02/2026")
Submit_btn = driver.find_element(By.XPATH,"//button[@class='submit-btn']").click()
single_upload = driver.find_element(By.XPATH,"//input[@id='singleFileInput']").send_keys(r"C:\Users\SHREE\OneDrive\Pictures\Screen_shot\add_cart2.png")
multiple_upload = driver.find_element(By.XPATH,"//input[@id='multipleFilesInput']").send_keys(r"C:\Users\SHREE\OneDrive\Pictures\Screen_shot\add_cart1.png")
time.sleep(20)

#row = WebDriverWait(driver, 10).until(
 #   EC.presence_of_element_located(
  #      (By.XPATH, "//td[normalize-space()='Internet Explorer']/parent::tr")
   # )
#)

row = driver.find_element(By.XPATH,"//td[normalize-space()='Internet Explorer']/parent::tr")
cols = row.find_elements(By.TAG_NAME,"td")

print("CPU:",cols[3].text)

