"""
from pprint import pprint
school = {
    'teacher': {
        'English': [
            {'name': 'Rohit', 'email': 'rohit@gmail.com', 'phone': 6546456},
            {'name': 'Rahul', 'email': 'rahul@gmail.com', 'phone': 56432343}
        ],
        'Maths': [],
    },
    'student': {
        '10th': [
            {'name': 'mohit', 'email': 'mohit@gmail.com', 'phone': 8866868686},
            {'name': 'akshay', 'email': 'akshay@gmail.com', 'phone': 876766766},
        ],
        '11th': [],
    },
    'admin': {
        'account': [],
        'admission': []
    }

}
# pprint(school)
# pprint(school['teacher']['English'])
pprint(school['student']['10th'][0])


fruit_price = {"Apple": 50, "Mango": 30, "Banana": 10, "Watermelon": 25}
fruit_purchased = {"Banana": 12,"Apple": 10, "Mango": 5, "Watermelon": 2}
# calculate total bill
total_bill = 0

for fruit, purches in fruit_purchased.items():
    f_price = fruit_price[fruit]
    fruit_bill = f_price * purches
    total_bill = total_bill + fruit_bill
    print(fruit, ":", f_price, ":", purches, ":", fruit_bill)

"""
