from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://practicetestautomation.com/practice-test-login/")

    # Using locators
    page.locator("#username").fill("student")

    page.locator("[name='password']").fill("Password123")

    page.get_by_role("button", name="Submit").click()

    page.wait_for_timeout(3000)

    browser.close()