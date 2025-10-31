# write a python program to create a dictionary from given string

str1="We are Learning Python"
word_list= str1.split(" ")
print(word_list)

result={}
for word in word_list:
    first_ch=word[0]
    result[first_ch]=word
print("The result is:",result)


# write a python program to get a nos from 1 to 20 and store even as key and their square as dict value.
print("."*100)
print()
evensquare={}
for i in range(1,21):
    if i%2==0:
        evensquare[i]=i**2
print(evensquare)

print("."*100)
print()
#Write a python program to get desire result -
# dict1={'a':[1,2,3],'b':[4,5,6]}
# output={'a':6}

dict1={'a':[1,2,3],'b':[4,5,6]}
output={}
for k,v in dict1.items():
    output[k]=sum(v)

print(output)