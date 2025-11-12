from datetime import datetime, timedelta

current_date = datetime.now()
print("Current date time is ",current_date)

print("Today's Date",current_date.date())
print("Today's Day",current_date.day)
print("Current month is", current_date.month)
print("Current year is",current_date.year)

# Date formatting

date_time_formatting= current_date.strftime("%y_%m_%d_%H_%M_%S")
print(date_time_formatting)

# Get 2 Dates today

print("2 days ago date:", (current_date - timedelta(days=2)).date())
print("2 days after date:", (current_date+timedelta(days=2)).date())

