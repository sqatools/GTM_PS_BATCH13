#print max,min,sum of list values
list1=[5,7,20.50,23,45]
print("max value:",max(list1))
print("max value:",sum(list1))

#program to get max value wihut using inbuilt function

list2=[5,7,9,23,80,56]
max_value =0
for value in list2:
    if value>max_value:
        max_value=value
    else:
          continue

    print(max_value)