dict_1 = {'a':23, 'b':30,'c': 77}

print(dict_1)

# add key & value in dictionary

dict_1['d']=92
dict_1['b']=31
print(dict_1)

# Apply loop

dict_2 = {'a':23, 'b':30,'c': 77}
for k,v in dict_2.items():
    print(k,':',v)

# Cretae dictinary from string
str1 = "We are learning python"
word_list = str1.split()
print(word_list)

result ={}
for word in word_list:
    first_char= word[0]
    result[first_char] = word
print(result)

# Get 1 to 20 numbers to store even values as key and value should be square of no
dict_3 ={}
result_1 ={}
for i in range(1,21):
    if i%2==0:
        result_1[i]= i**2
print(result_1)

# Get desired output = sum of values

dict_4 = {'a':(23,2,1), 'b':(30,2,6),'c': (77,1,2)}
output ={}
for k,v in dict_4.items():
    output[k]= sum(v)
print(output)


###### Methds of Dictionary ######
#1  Update method

dict_5 = {'a':23, 'b':30,'c': 77}
dict_6 ={'12':'Hello', '13': [5,2,3],'23': (2,3,5)}
dict_6.update(dict_5)
print(dict_6)

# Pop Method - Remove any specific data using the pop method and return the value
dict_7 = {'a':23, 'b':30,'c': 77}
val = dict_7.pop('b')
print('Remove val :', val)
print(dict_7)


# Del Keyword : Delete data from memory using 'Del' keyword.
dict_8 = {'p':3, 'q':80,'r':90}
del dict_8['r']
print(dict_8)
# delete entire dictionary from memory
"del dict_8"

# POP Item

dict_9 = {'k':30, 'K':76,'l':'Hello'}
val = dict_9.popitem()
print(val)
print(dict_9)


# List to dictionary
list_1 = ['s','t','u']
list_2 = [200,300,400]

dict_10 = zip(list_1,list_2)
print(dict_10)

dict_10= dict(zip(list_1,list_2))
print(dict_10)


## Key & Values in dictionary

dict_11= {'23':'Hi', '30':'John', '77': [12,23,27]}
print(dict_11.keys())
print(dict_11.values())

