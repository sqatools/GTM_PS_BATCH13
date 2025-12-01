import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def booking_site():
    driver=webdriver.Chrome()
    driver.get("https://www.booking.com/")
    driver.maximize_window()
    time.sleep(5)

    logo=driver.find_element(By.XPATH,"//a[@aria-label='Booking.com']")
    print("Logo text :",logo.text)

    savetxt=driver.find_element(By.XPATH,"//span[contains(text(),'Save up to 40% with Black Friday Deals')]")
    print("Deal text :",savetxt.text)



    stay=driver.find_element(By.XPATH,"//a[@id='accommodations']")
    stay.click()

    bookingtext = driver.find_element(By.XPATH, "//div[text()='Why Booking.com?']")
    print("Booking Text :", bookingtext.text)

    flight=driver.find_element(By.XPATH,"//a[@id='flights']")
    flight.click()

    #price=driver.find_element(By.XPATH,"(//button[contains(@aria-label, 'Prices in Indian Rupee')])[1]")
    #price.click()

    reg = driver.find_element(By.XPATH, "//a[@data-testid='header-sign-up-button']")
    reg.click()

    email = driver.find_element(By.NAME, "username")
    email.send_keys("latika.dh04@gmail.com")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    driver.find_element(By.XPATH, "//span[text()='Back to sign-in']").click()





booking_site()