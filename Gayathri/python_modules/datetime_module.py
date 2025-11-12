from datetime import datetime, timedelta

#to print the current date and time
current_date = datetime.now()
print(current_date)  # 2025-11-11 19:28:47.352848
print("today's date :", current_date.date())  # 2025-11-11
print("today's date value :", current_date.day) # 11
print("today's day name :", current_date.strftime("%A"))  # Tuesday
print("today's day name :", current_date.strftime("%a"))  # Tue
print("current Month :", current_date.month) # 11
print("current year :", current_date.year) # 2025

# date formatting
date_time_format = current_date.strftime("%d_%m_%Y_%H_%M_%S")
print("date time format value :", date_time_format)  # 11_11_2025_07_53_42
date_time_format2 = current_date.strftime("%d_%B_%Y_%H_%M_%S") #11_November_2025_19_28_47
# %b = month name : NOV
# %B = Complete Name of Month  : November
# %d = Date
# %m = month
# %Y = complete year name : 2025
# %y = short name of year : 25
# %H = Hours
# %M = Minutes
# %S = Second
print("date time format value :", date_time_format2)  # 11_November_2025_07_55_41


######### Get 2 date today #####
#for this use the import timedelta

print("2 days ago date: ", (current_date-timedelta(days=2)).date())  # 2025-11-09
print("2 days after date: ", (current_date+timedelta(days=2)).date()) # 2025-11-13