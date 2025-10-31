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

