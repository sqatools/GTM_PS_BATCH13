
dict1 = {'a' : 123, 'b' : 456, 'c' : 789}
print("dict1 : ", type(dict1))

# Add new key to dictionary
dict1['d'] = 100
dict1['b'] = 500
print("dict1 with added values :", dict1)
print("*"*50)

# Apply loop on dictionary
for k,v in dict1.items():
    print(k, "|", v)
print("*"*50)

# write a prg to create a dict from string
str1 = "We are learning Python"
# output = {'W' : We, 'a' : 'are'...}
wordlist = str1.split(" ")
print(wordlist)
res = {}
for word in wordlist:
    char = word[0]
    res[char] = word
print("new dict :",res)
print("*"*50)

# Write a python prg to get numbers from 1 to 20 and store even value as key and their square as value.
# dict2 = {2 :4, 4:16, 6:36,
result2 = {}
for i in range(1, 21):
    if i%2 == 0:
        result2[i] = i**2
    else:
        continue
print("result2  : ", result2)
print("*" * 50)

# write prg to get desired result
# dict1 = {'a' : 123, 'b' : 456, 'c' : 789}
# output = {'a' : 6, 'b':15} basically value has to be sum of all values
output= {}
dict1 = {'a': [1,2,3], 'b': [4,5,6],'c': [7,8,9]}
for k, v in dict1.items():
    output[k] = sum(v)
print("output :", output)

# dictionary methods
# update method - this method will combine 2 dict.
dict1 = {'a': 77, 'b': 88, 'c': 99}
dict2 = {12: 'Hello', 13: [15, 16, 17], 14: (3, 4, 5), 'a': 80}
dict2.update(dict1)
print("dict2 updated values : ", dict2)
# To remove any key/value use pop.
val = dict2.pop('a')
print("new dict2 val after removing'a' :", dict2)
print("*" * 50)

# if we yse del, it will remove the / key & value and if neeved variable from memory

# We can use zip function to combine 2 lists and put in dictionary. Its a predefined method
list1 = ['a', 'b','c']
list2 = [100, 200, 300]
dict5 = dict(zip(list1, list2))
print(dict5) # 'a' : 100,

# To get only keys and values list separate
dict6 = {12:'Hello', 6:'Hey',13 :'Bye', 9: 'Morning'}
print("list of keys in dict :", dict6.keys)
print("list of values in dict :", dict6.values)
#To get the value of certain key
print(dict6.get(13)) # output will give 'Bye'

print("*"*50)
# To get complex dict. structure

school = {
    'teacher': {
            'English' : [
               {'name': 'Rohit', 'email':'rohit@gmail.com', 'phone' : 6451245987},
               {'name': 'Renu', 'email' :'renu@gmail.com', 'phone' : 6451247777}
            ],
             'Math' : [15, 20, 35]
       },
    'student' :{
        '10th': [
            {'name': 'Anubhav', 'email':'anubhav@gmail.com', 'phone' : 7845145987},
            {'name': 'Anjali', 'email': 'anjali@gmail.com', 'phone' : 7651248745},
            ],
        '11th' : []
        },
    'admin': {
        'account' : [],
        'admission': []
    }
}
from pprint import pprint
pprint(school['teacher']['English'][0]['email'])
pprint(school['teacher']['Math'][2])
pprint(school['student']['10th'][1]['phone'])
pprint(school)

print("*"*50)
# Write a program to get the total bill amount for the fruits
fruit_price = {'Apple': 35, 'Banana': 40, 'Blueberry': 50, 'Pineapple': 75}
fruit_purchase = {'Apple': 10, 'Banana': 18, 'Blueberry': 2, 'Pineapple': 2}
total_bill = 0
for fruits, purchase in fruit_purchase.items():
    f_price = fruit_price[fruits]
    print("Price of fruits :", f_price)
    fruit_bill = f_price * purchase
    total_bill = fruit_bill+total_bill
    print(fruits, ":", purchase, ":", f_price, ":", total_bill)
    print ("Total Bill for fruits : ", total_bill)




