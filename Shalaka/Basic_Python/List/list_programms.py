#.1 Get the max value from list without using inbuild function
list1 =[4,5,90,34,23,30.78]
max_val =0
for val in list1:
    if val > max_val:
        max_val=val
    else:
        continue
print(max_val)

#2. Rempved duplicate
list2 =['shalaka','john','shalaka','Hello']
result2 =[]
for val in list2:
    if val not in result2:
        result2.append(val)
    else:
        continue
print(result2)


#.3 Move all positive no to left and negative no to right side
list3 =[-2,4,-5,-6,3,6]
positive_list =[]
negative_list =[]
for val in list3:
    if val>=0:
        positive_list.append(val)
    else:
        negative_list.append(val)
result3 = positive_list + negative_list
print(result3)

