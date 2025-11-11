from datetime import datetime

current_date=datetime.now()
print(current_date)
print("todays date",current_date.date)
print("todays day value",current_date.day)
print("todays month",current_date.month)
print("todays year",current_date.year)
print("todays day name",current_date.strftime("%A"))

date_time_format = current_date.strftime("%d_%m_%Y_%H_%M_%S")
print("date time format value :", date_time_format)