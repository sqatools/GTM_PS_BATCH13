# Properties
# --> List is a mutable datatype
# --> List can contain any types of data e.g.int, float, string, tuple,bool, list,dict.,set
# -->List follows positive and negative indexing.
# --> List contains values in square bracket.

list1 = [12,3.5,'hello',[5,6,7],[8,9,10],{'a': 42}, 'true']
print(list1,type(list1))

print(list1[2])
print(list1[-3])
print(list1[4])
print(list1[4][1])

print("*"*50)
# ------slicing in list----------
list3 = [5,8,9,2,15,'a','p','q','b']
print(list3[0:5])
print(list3[-5:-10:-1])
print(list3[5:9:1])
print(list3[::-1])

print("*"*50)

list2 = ['a','b','c',10,20,30]
for val in list2:
    print(val)

print("*"*50)

# list concatenation
l6 = [7,8,9]
l7 = [10,20,30]
l8 = l6+l7
print("l8 :", l8)

print("*"*50)

# list extend #to add one list to other
l4=[4,5,6]
l5 = [7,5.5,9]
l5.extend(l4)
print("l5 :-",l5)

print("*"*50)

#insert method : this method insert data at specific index
list5 = [8,9,10,4,7]
list5.insert(2, 100)
print("list5 = ",list5)

print("*"*50)

# Python program to calculate the sum of all elements from a list.
lista = [10,50,85,90.7]

var = 0
for value in lista:
    var += value

print(var)
