from datetime import datetime,timedelta
current_time = datetime.now()
print(current_time)
print("today day is", current_time.day)
print("today day is", current_time.month)
print("today day is", current_time.year)
date_time_format=current_time.strftime("%d/%m/%Y")
print(date_time_format)
date_time_formate2=current_time.strftime("%d+%B_%Y_%H_%M_%S")
print(date_time_formate2)
# %b = month name : NOV
# %B = Complete Name of Month  : November
# %d = Date
# %m = month
# %Y = complete year name : 2025
# %y = short name of year : 25
# %H = Hours
# %M = Minutes
# %S = Second
######### Get 2 date today #####

print("2 days ago date: ", (current_time-timedelta(days=2)).date())  # 2025-11-09
print("2 days after date: ", (current_time+timedelta(days=2)).date()) # 2025-11-13



