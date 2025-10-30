str3="good morning"
vowels="aeious"
count=0
for char in str3:
    print(char)
if char in vowels:
    count+=1
else:

     print("total words:",count)

###list##

list1=[2,3,5,"hello",(5,6,7),[6,7,8]]
print(list1[2])
print(list1[4])
print(list1[4][1])#0,1

#slicing#

list3= [5,8,9,2,15,'a','b','c','d']
print(list3[5:9])##from a it will print
print(list3[-1:-10:-1])###start ,step,stop

#append method
list8= [4,5,6]
list8.append(10)
print("list8:",list8)

#insert#

list10=[1,2,3,4,5,6]
list10.insert(6,7)
print("list10:",list10)