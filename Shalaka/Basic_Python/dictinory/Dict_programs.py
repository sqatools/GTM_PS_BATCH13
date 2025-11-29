## Get data from dictionary structure ##
"""from pprint import pprint
school = {
    'teacher': {
        'English' :[
            {'name':'Shalaka','email':'shalaka@gmail.com','phone': 23456},
            {'name':'John','email':'John@gmail.com','phone': 123456}

        ],
        'Maths' : []
        },
     'Student':{
        '10th':[
            {'name':'Smith','email':'smith@gmail.com','Phone': 23456},
            {'name':'Alex','email':'alex@gmail.com','Phone': 123456}
        ],
        '11th': []
     },

    'Admin': {
        'Accounts':[],
        'Admission':[]

     }
    }

pprint(school)
pprint(school['teacher']['English'][1]['phone'])


## Calculate the fruit price

fruit_price = {'Mango':60, 'Apple': 80, 'Banana' :50,'Chiku':30,'Orange' : 35}
fruit_purchase = {'Mango': 10, 'Banana' : 20, 'Apple': 5}
total_bill = 0
for fruit, purchase in fruit_purchase.items():
    price = fruit_price[fruit]
    bill= price*purchase
    print(fruit, ':', price,':',purchase,':', bill)

print('Total bill', bill)


###### Practice Prgrams######

print('1). Python Dictionary program to add elements to the dictionary.')

dict_1 = {'name': 'Shalaka', 'class': 12,'phone': 2330}
print(dict_1)

print('2). Python Dictionary program to print the square of all values in a dictionary.')
dict_2 ={'a': 5,'b':3, 'c': 6,'d' : 8}
print(dict_2)
square = 0

for val in dict_2:
    print( val,':',dict_2[val]**2)

"""
"""
print('3). Python Dictionary program to move items from dict1 to dict2.')

dict3 = {'name': 'john', 'city': 'florida', 'country': 'US'}
dict4 = {}
dict5 = dict3.copy()
for val in dict5:
    d1 = dict3.pop(val)
    dict4[val] = d1
print('dict4 :', dict4)
print('dict3 :', dict3)

#######################
print('4). Python Dictionary program to concatenate two dictionaries.')
dict_5 = {'Name': 'Harry', 'Rollno': 345, 'Address': 'Jordan'}
dict_6 = {'Age': 25, 'salary': '$25k'}

dict_5.update(dict_6)
print(dict_5)

#####################
print('5). Python Dictionary program to get a list of odd and even keys from the dictionary.')
dict_7 = {1: 25, 5: 'abc', 8: 'pqr', 21: 'xyz', 12: 'def', 2: 'utv'}
list1 = []
for val in dict_7:
    if val % 2 == 0:
        val = dict_7[list1]
        print(val)
"""

