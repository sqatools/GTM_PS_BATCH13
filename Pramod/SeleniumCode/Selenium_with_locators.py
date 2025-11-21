"""
List locators:
1). ID
2). NAME
3). LINK TEXT
4). PARTIAL LINK TEXT
5). CLASS
6). TAGNAME
7). CSS_SELECTOR
8). XPATH

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#open browser
driver = webdriver.Chrome()
# Maximize the browser
driver.maximize_window()
time.sleep(10)
driver.close()
