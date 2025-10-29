list1 = ["Adam", "Roger", "Mac", "Roger", "Alex", "Zidane", "Adam"]
list2 = []
for name in list1:
    if name not in list2:
        list2.append(name)
    else:
        continue
print(list2)

print('*'*50+"Find if Zidane is part of the list"+'*'*50)

for name in list1:
    if name != "Zidane":
        continue
    else:
        print(name+" is part of the list")
        break


print('*'*50)
list3 = [5, 7, 9, 23, 80, 56]
print("The maximum value is", max(list3))
print("The minimum value is", min(list3))
print("The average value is", int(sum(list3)/len(list3)))