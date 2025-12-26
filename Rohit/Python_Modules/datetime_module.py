from datetime import datetime , timedelta

current_time = datetime.now()
print(current_time) # 2025-11-11 08:10:13.191096
print("current date :",current_time.date()) # 2025-11-11
print("current particular date :",current_time.day) # 11
print("Current day :",current_time.strftime("%A")) # Tuesday
print("current day :",current_time.strftime("%a")) # Tue
print("current month :", current_time.month) # 11
print("current year :",current_time.year) # 2025

# date formatting
date_time_format = current_time.strftime("%d_%m_%Y_%H_%M_%S")
print("date_time_formate value :",date_time_format) # 11_11_2025_08_18_45

date_time_format2 = current_time.strftime("%d_%B_%Y_%H_%M_%S")
# %b = month name : NOV
# %B = Complete Name of Month  : November
# %d = Date
# %m = month
# %Y = complete year name : 2025
# %y = short name of year : 25
# %H = Hours
# %M = Minutes
# %S = Second
print("date_time_format2 value :",date_time_format2) # 11_November_2025_08_20_21

######### Get date 2 date Ago #####
print("2 days ago date :",current_time-timedelta(days=2)) # 2025-11-09 08:22:12.627689
print("Display 2 days ago date :", (current_time-timedelta(days=3)).date()) # 2025-11-08

print("2 days after date :", current_time+timedelta(days=2)) # 2025-11-13 08:25:21.726177
print("Display 2 days after date :", (current_time+timedelta(days=3)).date()) # 2025-11-14

