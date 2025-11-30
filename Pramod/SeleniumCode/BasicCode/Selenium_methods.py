import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://sqatools.in/dummy-booking-website/")

# get current url
print("url :", driver.current_url)

# get website title
print("title :", driver.title)

# get heading text with the help of text method.
heading = driver.find_element(By.TAG_NAME, "h1").text
print("website heading :", heading)

# check given element is displayed, enabled, selected.
radio_btn = driver.find_element(By.ID, "oneway")

print("radio button is displayed :", radio_btn.is_displayed())
print("radio button is enabled :", radio_btn.is_enabled())
print("radio button is selected before click :", radio_btn.is_selected())
time.sleep(5)
radio_btn.click()
print("radio button is selected after click :", radio_btn.is_selected())

time.sleep(5)

# Get attribute value, get url from link text
login_link = driver.find_element(By.LINK_TEXT, "Login Page")
print("link url :", login_link.get_attribute('data-id'))

# Forward, Back, Refresh.
login_link.click()
time.sleep(5)
driver.save_screenshot(r"E:\Filesdata\Batch13\login_page_image1.png")

# back to dummy page
driver.back()
time.sleep(5)
driver.save_screenshot(r"E:\Filesdata\Batch13\dummy_page_image2.png")

# move forward to login
driver.forward()
time.sleep(5)
driver.save_screenshot(r"E:\Filesdata\Batch13\login_page_image3.png")

# perform refresh operation.
driver.refresh()




driver.close()





