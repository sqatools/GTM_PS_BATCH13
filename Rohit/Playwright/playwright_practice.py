from playwright.sync_api import sync_playwright

def test_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com")
        page.fill('textarea[name="q"]', "Job for selenium in Python in Pune location")
        page.keyboard.press("Enter")
        page.wait_for_timeout(3000)
        print(page.title())
        browser.close()





