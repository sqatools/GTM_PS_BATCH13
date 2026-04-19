from selenium.webdriver.common.by import By

Name = (By.XPATH,"//input[@placeholder='Enter Name']")
Email = (By.XPATH,"//input[contains(@placeholder,'Enter EMail')]")
Phone = (By.XPATH,"//input[starts-with(@placeholder,'Enter Phone')]")
Address = (By.XPATH,"//textarea[@id='textarea']")
Gender_Male = (By.XPATH,"//input[@value='male']")
Day_Wednesday = (By.XPATH,"//label[starts-with(@for,'wednesday')]")
Country = (By.XPATH,"//select[contains(@id,'country')]")