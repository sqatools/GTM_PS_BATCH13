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

