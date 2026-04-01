from selenium.webdriver.common.by import By

user_name = (By.NAME,"username")
Password = (By.NAME,"password")
Login_btn = (By.XPATH,"//button[@type='submit']")

#recruitment
Recruitment = (By.XPATH,"//span[text()='Recruitment']")
Job_title = (By.XPATH,"//label[text()='Job Title']/../following-sibling::div//div[text()='ab1']")
Vacancy= (By.XPATH,"//label[text()='Vacancy']/following::div[contains(@class,'oxd-select-text-input')][1]")
Hiring_Manager = (By.XPATH,"//label[text()='Hiring Manager']/following::div[contains(@class,'oxd-select-text-input')][1]")
Status = (By.XPATH,"//label[text()='Status']/following::div[contains(@class,'oxd-select-text-input')][1]")
Candidate_Name = (By.XPATH,"//label[text()='Candidate Name']/following::div[contains(@class,'oxd-autocomplete-text-input oxd-autocomplete-text-input--active')][1]")
Keywords = (By.XPATH,"//label[text()='Keywords']/following::input[contains(@class,'oxd-input oxd-input--active')][1]")
start_Date_of_Application = (By.XPATH,"//label[text()='Date of Application']/following::input[contains(@class,'oxd-input oxd-input--active')][1]")
end_Date_of_Application = (By.XPATH,"//input[@placeholder='To']")
Method_of_Application = (By.XPATH,"//label[text()='Method of Application']/following::div[contains(@class,'oxd-select-text oxd-select-text--active')][1]")