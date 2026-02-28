# Write a prg. to remove duplicate words from given string

str1= "rahul preeti partha arun rahul preeti"
wordlist=str1.split(" ")
print(wordlist)
result = ""
for word in wordlist:
    if word not in result:
        result = result + word +" "
    else:
        continue
        print(result)
print("Final Result :", result)

# Write a prg. to get longest word from given string
str2 = 'We are learning Python Programming, it is easy to learn'
word_list = str2.split(" ")
long_len = 0
for word in word_list:
    print(word, len(word)) # This will print the word and its length.
    word_len = len(word)
    if word_len > long_len:
        if word_len > long_len:  # 2 > 0 | 3 > 2 | 8 > 3 | 6 > 8 | 11 > 8
            long_len = word_len  # 2, 3, 8, 11
        long_word = word  # we, Are, Learning, Programming
    else:
        continue

list_b = [6,7,8,9,45]
list_b.remove(9)
print("list_b :", list_b) #(output - all numbers except 9)

print("*"*50)

#Pop method - this removes method from default index position.
#default index value is -1
#this method will return the removed value that we can store in a variable

list_c = [5,7,2,15,18]
v1 = list_c.pop()
print("removed value  :", v1)
print ("list _C", list_c)

#to remove from specific index
v2 = list_c.pop(1)
print("removed value :", v2)
print("list_C :", list_c)

# clear method : clear all data from list.

list1 = [5,7,9,2]
list1.clear()
print("list1 :", list1) # output - blank list

# copy method - there are 2 methods - deep copy and shallow copy
# copy file data :
list_d = [4,7,9,45]
list_e = list_d #this is a shallow copy. so any modification done in list d will reflect in list e as well.
list_e.append(100)
list_d.append(200)
print("list_e :", list_e)
print("list_d :", list_d)

# Deep copy -In this concept we have to copy method to create a list and modification done in one list will not impact the other

list_x = ['a','b','c']
list_y = list_x.copy()
list_x.append('d')
list_y.append(100)

print("list_x :", list_x)
print("list_y :", list_y)

#############################
#sort method: Sort in asc/desc method

list1=[5,8,6,7,12,45]
#sort in ascending order
list1.sort()
print("list1 :", list1)

list2=[5,8,15,17,82,87]
#sort in descending order
list2.sort(reverse = True) # We have to mention reverse=true to see the desc.
print("list2 :", list2)

# reverse method : this will reverse the entire list
list_n = [8,14,'Functions',27,42,'true']
list_n.reverse()
print("list_n :", list_n)


# Write a python program to get all even values from list
list_x = [4,7,8,9,2,6,12,15,16]
output = []
for val in list_x:
    if val%2 == 0:
        output.append(val)
    else:
        continue
print("output ", output)

#solve above prg with list comprehension
result = [x for x in list_x]

# write a prg to get all req. output values from list
list1 = [4,7,9,12]
# output = [(4=even)
output =[]
for val in list1:
    if val%2 == 0:
        output.append((val, 'even'))
    else:
        output.append((val, 'odd'))
print("output :", output)

# Write the same in list comprehension
#result2 = [y, 'even') if y % 2 == 0 else(y,'odd') for y in list1]

# Write a Python program to replace the second occurrence of any char with the special character $.
# Input = “Programming”
# Output = “Prog$am$in$”

str1 = 'programming'
st2 = " "
for char in str1:
    if char in st2:
        st2 = st2 + '$'
    else:
        st2 = st2 + char
print("Revised string :", st2)
print("_"*50)