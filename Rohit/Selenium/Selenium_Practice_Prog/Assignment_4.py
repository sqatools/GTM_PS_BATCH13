import time
from calendar import month

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationexercise.com/login")
action = ActionChains(driver)

Signup = driver.find_element(By.XPATH,"//a[@href='/login']").click()
driver.find_element(By.XPATH,"//input[@data-qa='signup-name']").send_keys("Dheeraj Chavan")


Password = driver.find_element(By.XPATH,"//input[@data-qa='signup-email']")
Password.send_keys("manalip7890@gmail.com")
time.sleep(2)

driver.find_element(By.XPATH,"//button[@data-qa='signup-button']").click()

driver.find_element(By.ID,"id_gender1").click()
driver.find_element(By.ID,"password").send_keys("Karad@123")
driver.find_element(By.NAME,"days")
Days = driver.find_element(By.XPATH,"//option[text()='10']").click()
driver.find_element(By.ID,"months")
months = driver.find_element(By.XPATH,"//option[text()='July']").click()
driver.find_element(By.ID,"years")
years = driver.find_element(By.XPATH,"//option[text()='2019']").click()

driver.find_element(By.ID,"newsletter").click()
driver.find_element(By.NAME,"first_name").send_keys("Dheeraj")
driver.find_element(By.NAME,"last_name").send_keys("Chavan")
driver.find_element(By.NAME,"company").send_keys("Infosys")
driver.find_element(By.ID,"address1").send_keys("452A Shaniwar Peth")
driver.find_element(By.ID,"address2").send_keys("39B Shivaji Chowk")
driver.find_element(By.ID,"country")
driver.find_element(By.XPATH,"//option[text()='India']").click()
driver.find_element(By.ID,"state").send_keys("Maharastra")
driver.find_element(By.NAME,"city").send_keys("Karad")
driver.find_element(By.ID,"zipcode").send_keys("415110")
driver.find_element(By.ID,"mobile_number").send_keys("8734567909")
driver.find_element(By.XPATH,"//button[@data-qa='create-account']").click()
print(driver.title)
driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()

def scroll():
    action.scroll_by_amount(700,700)
    action.perform()

scroll()

def hovering_items():
    Feature_item = driver.find_element(By.XPATH,"//img[@src='/get_product_picture/1']")
    action.move_to_element(Feature_item).perform()
    time.sleep(5)

hovering_items()
time.sleep(5)

wait = WebDriverWait(driver, 10)
add_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@data-product-id='1' and contains(text(),'Add to cart')]")))

# scroll into view + action click (best for hover elements)
driver.execute_script("arguments[0].click();", add_cart_button)
action.move_to_element(add_cart_button).click().perform()
time.sleep(5)
driver.save_screenshot(r"C:\Users\SHREE\OneDrive\Pictures\Screen_shot\add_cart2.png")
driver.find_element(By.XPATH,"//p[@class='text-center'] //a[@href='/view_cart']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Proceed To Checkout']").click()
time.sleep(5)
driver.find_element(By.NAME,"message").send_keys("Please place order proper and delilver on time")
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Place Order']").click()
time.sleep(5)
Name_of_card = driver.find_element(By.NAME,"name_on_card").send_keys("Debit Cars")
card_num = driver.find_element(By.XPATH,"//input[@name='card_number']").send_keys("4673673662234")
CVC = driver.find_element(By.NAME,"cvc").send_keys("234")
Expiration = driver.find_element(By.NAME,"expiry_month").send_keys("11")
Year = driver.find_element(By.NAME,"expiry_year").send_keys("2028")
comfirm_button = driver.find_element(By.XPATH,"//button[@data-qa='pay-button']").click()
time.sleep(5)
continue_button = driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()
time.sleep(5)
driver.back()
time.sleep(5)
download_Invoice = driver.find_element(By.XPATH,"//a[text()='Download Invoice']").click()
time.sleep(5)



