"""
Implicit wait
Explicit wait
Fluent Wait - no of iterations 
static wait
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get()
