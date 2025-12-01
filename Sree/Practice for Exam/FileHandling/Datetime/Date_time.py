from datetime import datetime,timedelta

current_date = datetime.now().date()
print(current_date.today())
print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.strftime("%A"))
print(current_date.strftime("%d/%m/%Y/%H/%M/%S"))
print('Get 2 days+/-today','-'*44)
print(current_date-timedelta(days=4))
print(current_date+timedelta(days=4))
print('-'*50)
Today=datetime.now()
print('1.',Today)  #1. 2025-11-24 08:46:52.637302
print('2.',Today.date())  #2025-11-24
print('3.',Today.day)
print('4.',Today.month)
print('5.',Today.year)
print('6.',"day name",Today.strftime("%A")) #6. day name Monday
print('7.',"day name",Today.strftime("%a")) #7. day name Mon
print('8,',Today.strftime("%m/%d/%Y/%H/%M/%S"))  #8, 11/24/2025/08/46/52
print('9.',Today-timedelta(days=2))
print('9.',(Today-timedelta(days=2)).date())  # will get only Date
print('10.',Today+timedelta(days=2))

print('10.',(Today+timedelta(days=2)).date())  # will get only Date