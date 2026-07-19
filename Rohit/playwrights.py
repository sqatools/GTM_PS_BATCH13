from playwright.sync_api import sync_playwright
from selenium import webdriver

with sync_playwright() as p:
    browser = webdriver.Chrome()