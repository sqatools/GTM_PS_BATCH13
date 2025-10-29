

lis1=[1,2,3,4,5,6,7,8,9]
lis1.clear()
#lis1.remove(2)
#lis1.pop()
#lis1.pop(2)

listx=["hello"]
listy=["world"]
listy=listx
print(listx)
print(listy)

list123=[1,2,3,4,5,6,7,8,9]
list123.sort()
list123.sort(reverse=True)
print(list123)

##########################

list_x = [1,2,3,5, 7, 9, 23, 4, 78, 'abc', 'xyz']
list_x.reverse()
print("list x :", list_x)

list1 = [4, 7, 9, 2, 8, 12, 11]
output = []

for val in list1:
    if val%2 == 0:
        output.append(val)
    else:
        continue

print("output :", output)  # [4, 2, 8, 12]

# solve above program to with list comprehension
result = [abc for abc in list1 if abc%2 == 0]
print("Result :", result)

#####################################################

list_a=[1,2,3,4,5,6,7,8,9]
print(max(list_a))
print(min(list_a))
print(sum(list_a))

#code without using max inbuilt function
x=0
for i in list_a:
    if x>i:
        x=i
    else:
        continue

print(i)

#code to remove duplicate vales in list
list_dup=[1,2,3,2,3,4,1,5,6,7,4,8,9]

x=[]
for i in list_dup:
    if i not in x:
        x.append(i)
    else:
        continue
print(x)

#code to move all positive value to left side and -ve values to right side
list_pn=[1,-2,3,-4,5,-6,7,-8,9]
listp=[]
listn=[]

for i in list_pn:
    if i>0:
      listp.append(i)
    else:
        listn.append(i)
a=listp+listn
print(a)




















