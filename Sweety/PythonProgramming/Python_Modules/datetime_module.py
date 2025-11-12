from datetime import datetime, timedelta

current_date = datetime.now()
print("Entire Date with Timestamp: ", current_date) #2025-11-11 12:09:55.251744
print("Current Date YYYY/MM/DD: ", current_date.date()) #2025-11-11
print("Current Date: ", current_date.day) #11
print("Current Month: ", current_date.month) #11
print("Current Year: ", current_date.year) #2025
print("Current Day: ", current_date.strftime("%A")) #Tuesday
print("Current Day: ", current_date.strftime("%a")) #Tue

########################### date formatting ###################################
date_time_format = current_date.strftime("%d/%m/%Y:%H:%M:%S")
print("Date and Time Format: ", date_time_format) #11/11/2025:12:32:39
date_time_format2 = current_date.strftime("%d/%B/%Y:%H:%M:%S") #11/November/2025:12:34:13
print("Date and Time Format2: ", date_time_format2)
# %b = month name : NOV
# %B = Complete Name of Month  : November
# %d = Date
# %m = month
# %Y = complete year name : 2025
# %y = short name of year : 25
# %H = Hours
# %M = Minutes
# %S = Second

######### Get 2 days ago ###########
print("2 days ago date: ", (current_date-timedelta(days=2)).date()) #2025-11-09
print("2 days after date: ", (current_date+timedelta(days=2)).date()) #2025-11-13



