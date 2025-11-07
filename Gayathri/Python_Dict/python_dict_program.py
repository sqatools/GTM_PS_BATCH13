#31st-oct-25

# write a python program to create a dictionary from given string.
str1 = "We are learning Python"
# output = {"W": We, "a": "are", "l": "learning", "P": "Python"}

word_list = str1.split()
print(word_list) #['We', 'are', 'learning', 'Python']
result = {} #empty dictionary
for word in word_list:
    #we need the 1st character from each word, which is index of 0
    first_char = word[0]
    print(first_char,end=" ") #W a l P
    result[first_char] = word
    print(result)
print("the newly formed dictionary:", result)
#the newly formed dictionary: {'W': 'We', 'a': 'are', 'l': 'learning', 'P': 'Python'}

print("_" * 50)
#######################
# write a python program to get number from 1 to 20 and store even value as key and their square as dict value.
# dict2 = {2 :4, 4: 16, 6: 36, 8: 64, 9: 81}
result = {}
for i in range(1, 21):
    if i % 2 == 0:
        result[i] = i**2
    else:
        continue
print(result)
#{2: 4, 4: 16, 6: 36, 8: 64, 10: 100, 12: 144, 14: 196, 16: 256, 18: 324, 20: 400}

###############################################
# Q3:  write a python program to get desire result:
dict1 = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
# output = {'a' : 6, 'b': 15, 'c': 24}

output= {}
for k,v in dict1.items():
    output[k] = sum(v)
print(output)
#{'a': 6, 'b': 15, 'c': 24}

################################################################
#4th Nov
# program to practice"
fruit_price = {"Apple": 50, "Mango": 30, "Banana": 10, "Watermelon": 25, "lichi": 30, "Pinapple": 60}
fruit_purchased ={"Banana": 12,"Apple": 10, "Mango": 5,  "Watermelon": 2}
# calculate total bill
total_bill = 0
for fruit, purches in fruit_purchased.items():
    f_price = fruit_price[fruit]
    #print("f_price:",f_price)
    fruit_bill = f_price * purches
    #print("fruit_bill:",fruit_bill)
    total_bill = total_bill + fruit_bill
    #print("*"*50)
    print(fruit, ":", f_price, ":", purches, ":", fruit_bill)
print("_"*20)
print("Total bill :", total_bill)
# Total bill : 820

"""
Banana : 10 : 12 : 120
Apple : 50 : 10 : 500
Mango : 30 : 5 : 150
Watermelon : 25 : 2 : 50

"""



