import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.edge.options import Options as Edge_Options


browser = "edge"
headless = True
driver = None

if browser.lower() == "firefox":
    opt = Firefox_Options()
    if headless:
        opt.add_argument("-- headless")
        driver = webdriver.Firefox(options=opt)

elif browser.lower() == "edge":
    opt = Edge_Options()
    if headless:
        opt.add_argument("--headless")
        driver = webdriver.Edge(options=opt)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationexercise.com/contact_us")

time.sleep(5)
driver.close()