# Add new key to dictionary #########
d1={'a':111,'b':222,'c':333}
d1['d']=444
d1['e']=555
d1['c']=666
print(d1)  # {'a': 111, 'b': 222, 'c': 666, 'd': 444, 'e': 555}
#print(d1.items())  ## ([('a', 111), ('b', 222), ('c', 666), ('d', 444), ('e', 555)])
# Apply loop on dictionary  #########
for k,v in d1.items():
    print(k,":",v)
print("_" * 50)
#######################
# write a python program to create a dictionary from given string.
# output = {"W": We, "a": "are", "l": "learning", "P": "Python"}
str1 = "We are learning Python"
wordslist= str1.split(" ")
print(wordslist)  # ['We', 'are', 'learning', 'Python']
result={}
for i in wordslist:
    firstchar=i[0]
    result[firstchar]=i
    print(result)
print("Result :", result)
print('-'*30)
string='we have two cars'
sep_words =string.split(" ")
print(sep_words)
dic={}
for i in sep_words:
     first_char =i[0]
     dic[first_char]=i
print(dic)
###################################
# write a python program to get number from 1 to 20 and store even value as key and their square as dict value.

result={}
for i in range(1,21):
    if i%2==0:
        result[i]=i**2
    else:
        continue   #Odd numbers → skip (because of continue)
print(result)
##########################################
# Q3:  write a python program to get desire result:
dict1 = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}

output={}
for k,v in dict1.items():
    output[k]=sum(v)
print(output)
########################## # dictionary methods
# 1.# update method:  this method combine 2 dicts data
d1={'a':60,'b':70,'c':80}
d2={'d':20,'e':10,'f':50}
d1.update(d2)
print('updated',d1)
## 2., # pop() method :  This method remove any specific data using key and return it.
d3 = {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'a': 77, 'b': 88, 'c': 99}
d7=d3.pop('b')
print('pop',d7)  # return value: 88
print(d3)
# 3 # delete data using del keyword
d4={'d':20,'e':10,'f':50}
del d4['f']
print('del keyword',d4)
# this will remove entire variable from memory.
#del d4
#print('deleted',d4)
# popitem() method :  removes and returns a key–value pair  #Removes the last inserted key–value pair
d5 = {12: 'Hello', 13: [5, 6, 7], 'b': 88, 'c': 99}
d6=d5.popitem()
print('popitem:',d6) # popitem: ('c', 99)- returned value
print(d5)
######################################  zip  #######
l1=[1,2,2,4,6]
l2=[500,700,700,00,100,900,700]
d8=dict(zip(l1,l2))
print('zip function',d8)
########################   # keys and values.   ############
d5 = {12: 'Hello', 13: [5, 6, 7], 'b': 88, 'c': 99}
print('give all keys',d5.keys())
print('give all values',d5.values())
###########          # get method: get value with the help of key
print('get values',d5.get('c'))
print('-'*30)
##############################################################
from pprint import pprint

# get data from dictionary
##pprint is used for pretty-printing complex data structures
# (like dictionaries, lists, nested objects).

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
pprint(school['teacher']['English'][1]['phone'])
pprint(school)
########################################################################
print('='*30)
school= {'Teacher':{
    'English':[
        {'teacher name':'Ram','teacher email':'Ram@gmail.com','phno':12345678},
        {'teacher name':'Shame','teacher email':'Sham@gmail.com','phno':9876543}

],
    'Math':[]

},
    'Students':{
        '10thgrade':[
            {'Studentname':'kumar','email':'kum@gamil.com','ph':76543209},
            {'Studentname':'Santhosh','email':'san@gamil.com','ph':76543209},

        ] ,
        '11thgrade':[
            {'stuname':'Geeta','email':'get@gmail.com','ph':98765432},
        {'stuname': 'sita', 'email': 'sit@gmail.com', 'ph': 98765432}
        ]

    },
    'staff':{
        'PT':[
            {'ptname':'Clair','email':'clar@gmail.com','ph':98765432}
        ],
        'principle':[{'princename':'Max','email':'Max@gmail','ph':9876541}]
    }

}
pprint(school['Teacher']['English'][0]['phno'])
pprint(school['Teacher']['English'][0]['teacher name'])
pprint(school['Students']['11thgrade'][1]['email'])
#pprint(school)
##########################    # calculate total bill      ########
Allfruit_price = {"Apple": 50, "Mango": 30, "Banana": 10, "Watermelon": 25, "lichi": 30, "Pinapple": 60}
fruit_purchased = {"Banana": 12, "Apple": 10, "Mango": 5, "Watermelon": 2}

total_bill = 0  # total should be a number, not a dictionary

##for k,v in dic.items():

for fruit, purchased in fruit_purchased.items():
    f_fruit = Allfruit_price[fruit]
    eachfruitprice = f_fruit * purchased
    total_bill += eachfruitprice  # correct way to add
    print(fruit, ":", f_fruit, ":", purchased, ":", eachfruitprice)

print('total bill =', total_bill)
###########  move items from dict1 to dict2.  #simply update dict2 with dict1 and then clear dict
dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
dict2 = {}
dict2.update(dict1)
print(dict1)
dict1.clear()
print(dict1)
print('dict2:',dict2)
#################### Concatenate two dictionaries to form a single dictionary using update()
#   get a list of odd and even keys from the dictionary.
d1 = {1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
even_keys=[]
odd_keys=[]
for key in d1.keys():
    if key%2==0:
        even_keys.append(key)
    else:
        odd_keys.append(key)
print("even keys:",even_keys)
print("odd keys:",odd_keys)
##### To both key and value

even_kvpair=[]
odd_kvpair=[]
for key,value in d1.items():
    if key%2==0:
        even_kvpair.append((key,value))
    else:
        odd_kvpair.append((key,value))
print("even,k:v",even_kvpair)
print('odd,k:v',odd_kvpair)
##   to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
print('even and odd {}','-'*30)
list1 = [4, 5, 6, 2, 1, 7, 11]
dic={}
for i in list1:
    if i % 2==0:
        dic[i]=i**2

    else:
        dic[i]=i**3
print(dic)

#3###remove duplicate values
d1 = {'a':12,'b':2,'c':12,'d':5,'e':35,'f':5}

d2 = {}
for k,v in d1.items():
    if v not in d2.values():   # .valuesmethod
        d2[k] = v

print("remove dupval",d2)
######### to create a dictionary from the string.
string = "SQAToolss"
dict1 = {}
for char in string:
    dict1[char] = string.count(char)  #countmethod
print(dict1)
"""
output: {'S': 1, 'Q': 1, 'A': 1, 'T': 1, 'o': 2, 'l': 1, 's': 2}
This function counts how many times that character appears in the entire string.
"""
##########    sort a dictionary using keys.  sorted() method
for key in sorted(d1):
    print('sort with keys:',key,d1[key])

for key, value in sorted(d1.items(), key=lambda a: a[1]):  # tells Python to sort by value instead of key
    print('sort with values',key,':', value)
#####
d1 = {'a':12,'b':2,'c':12,'d':5,'e':35,'f':5}
for k in sorted(d1):
    print(k,d1[k])
# sorted by values
########### key exists in the dictionary or not.##############
D1 = {'city':'HYD','state':'AP'}
count = 0

for key in D1.keys():
    if key == "Country":
        count += 1

if count > 0:
    print("Key exists")
else:
    print("Key does not exists")
##########             iterate over a dictionary
D1 = {'food':'burger','type':'fast food'}

for I in D1:
    print(I,D1[I])
######           to map two lists into a dictionary.
a = [ 'name', 'sport', 'rank', 'age']
b = ['Virat', 'cricket', 1,  32]
C= dict(zip(a,b))
print('mapping 2lists',C)
#####  find maximum and minimum values in a dictionary.
d1 = {'a':12,'b':2,'c':12,'d':5,'e':35,'f':5}
list=[]
for i in d1.values():
    list.append(i)
#list.sort() no need
print('printinglist',list)
print('Max val',max(list))
print('Max val',min(list))
#####  group the same items into a dictionary value.
"""from collections import defaultdict

list1 = [1,3,4,4,2,5,3,1,5,5,2]
print("The original list : ",list1)

dict1 = defaultdict(list)
for val in list1:
    dict1[val].append(val)
print("Similar grouped dictionary :" ,dict1)
"""
##############  check whether a dictionary is empty or not.
dict1 = {}

if len(dict1) > 0:
    print("Dictionary is not empty")
else:
    print("Dictionary is empty")
#########  add two dictionaries if the keys are the same then add their value.
D1 = {'x':10,'y':20,'c':50,'f':44 }
D2 = {'x':60,'c':25,'y':56}

for key in D1:
    if key in D2:   ## has to takd same key in both places
        D2[key] += D1[key]
    else:
        D2[key] = D1[key]

print(D2)
#####  print all the unique values
l1 = [{'name1':'robert'},{'name2':'john'},{'name3':'jim'},
         {'name4':'robert'}]
l2 = []
for val in l1:
    for j in val.values():
        if j not in l2:
            l2.append(j)

print(l2)
#######   find the length of dictionary values
D1 = {1:'sql',2:'tools',3:'python'}
D2 = {}

for val in D1.values():
    D2[val] = len(val)

print(D2)
####### given a dictionary to a list of tuples.

D1 = {'a':19,'b':20,'c':21,'d':20}
l = list(D1.items())

print(l)
