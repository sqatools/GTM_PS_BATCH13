import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_option
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.edge.options import Options as edge_options

browser = "edge"
headless = True       # headless Ture means browser will not get open and false means browser will get open will automation
driver = None

if browser.lower() == "chrome":
    opt = chrome_option()
    if headless:
        opt.add_argument("--headless")
    driver = webdriver.Chrome(options=opt)


elif browser.lower() == "firefox":
    opt = firefox_options()
    if headless:
        opt.add_argument("--headless")
    driver = webdriver.Firefox(options=opt)

elif browser.lower() == "edge":
    opt = edge_options()
    if headless:
        opt.add_argument("--headless")
    driver = webdriver.Edge(options=opt)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/dummy-booking-website/")

fromcity_elem = driver.execute_script("return document.getElementById('fromcity');")
fromcity_elem.send_keys("Mumbai")
fromcity_elem = driver.execute_script("return document.getElementById('destcity');")
fromcity_elem.send_keys("Pune")
time.sleep(5)
driver.save_screenshot("page_snapshot.png")
title = driver.execute_script("return document.title;")
print("website title :", title)
URL = driver.execute_script("return document.URL")
print("current URL:", URL)

win_height = driver.execute_script("return window.outerHeight;")
win_width = driver.execute_script("return window.outerWidth;")

print("window height :", win_height)
print("window width :", win_width)
time.sleep(5)

# scroll to height of the page.
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

driver.close()
