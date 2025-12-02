import time
from logging import exception
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def launch_the_goibibo_site(browser = "Chrome"):
    driver=None
    if browser.lower() == 'chrome':
        driver=webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver=webdriver.firefox()
    elif browser.lower() == 'edge':
        driver=webdriver.edge()

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.goibibo.com/")
    return driver
    time.sleep(5)

def book_flight(driver):

    wait = WebDriverWait(driver, 10)

    # Cancel the login-sign up pop-up
    try:
        close_popup= driver.find_element(By.XPATH,"//span[@class='logSprite icClose']")
        close_popup.click()
    except Exception as e:
        print("pop up not found",e)

    # Enter the "From" city - Mumbai
    from_city=driver.find_element(By.XPATH,"//input[@id='fromCity']")
    from_city.click()

    enter_from_city=driver.find_element(By.XPATH,"//input[@placeholder='From']")
    enter_from_city.send_keys("Mumbai")

    mumbai_option = wait.until(ec.element_to_be_clickable((By.XPATH, "//span[normalize-space()='BOM']")))
    mumbai_option.click()
    print("From city Mumbai is selected")
    time.sleep(5)

    # Enter the "To" City - Jaipur
    to_city=driver.find_element(By.XPATH,"//input[@id='toCity']")
    to_city.click()

    enter_to_city=driver.find_element(By.XPATH,"//input[@placeholder='To']")
    enter_to_city.send_keys("Jaipur")

    jaipur_option=wait.until(ec.element_to_be_clickable((By.XPATH,"//span[normalize-space()='JAI']")))
    jaipur_option.click()
    print("To city Jaipur is selected")
    time.sleep(5)

    # click the date picker
    click_on_departure=wait.until(ec.element_to_be_clickable((By.XPATH,"//span[text()='Departure']")))
    click_on_departure.click()

    departure_date = "Sat Jan 10 2026"
    select_the_d_date=wait.until(ec.element_to_be_clickable((By.XPATH,f"//div[@aria-label='{departure_date}']")))
    select_the_d_date.click()
    print("Departure Date is Saturday, 10 January 2026")
    time.sleep(5)

    click_on_return=wait.until(ec.element_to_be_clickable((By.XPATH,"//span[text()='Return']")))
    click_on_return.click()

    return_date ="Sat Jan 17 2026"
    select_the_r_date=wait.until(ec.element_to_be_clickable((By.XPATH,f"//div[@aria-label='{return_date}']")))
    select_the_r_date.click()
    print("Return Date is Saturday, 17 January 2026")
    time.sleep(5)

    traveller_count=driver.find_element(By.XPATH,"//span[@class='lbl_input appendBottom5']")
    traveller_count.click()

    wait.until(ec.presence_of_element_located((By.XPATH,"//li[@data-cy='adults-2']"))).click()

    apply_btn=wait.until(ec.element_to_be_clickable((By.XPATH,"//button[text()='APPLY']")))
    apply_btn.click()

    submit_btn=wait.until(ec.element_to_be_clickable((By.XPATH,"//a[text()='Search']")))
    submit_btn.click()
    print("Searching the flights...")

    try:
        got_it_pop_up=driver.find_element(By.XPATH,"//button[text()='OKAY, GOT IT!']")
        got_it_pop_up.click()
    except Exception as e:
        print("Pop not came",e)

    time.sleep(10)




driver = launch_the_goibibo_site()
book_flight(driver)
