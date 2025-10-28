"""
#  clear method
list1 = [8, 11, 58, 0, 3, 4]
list1.clear()
print("list1 :", list1)

"""
#  copy() method
# shallow copy

"""
list2 = [8, 11, 58, 0, 3, 4]
list3 = list2
list2.append(10)
list3.append(50)
print("list2 :", list2)
print("list3 :", list3)
            

list_d = [4, 7, 9, 23]
list_e = list_d
list_e.append(100)
list_d.append(200)

print("list_e :", list_e)
print("list_d :", list_d)

"""
"""
# deep copy

list_a = [90, 5, 34, 600, 457]
list_b = list_a.copy()
list_a.append('lol')
list_b.append(84)
print("list_a :", list_a)
print("list_b :", list_b)
"""
"""
# sort method

list4 = [45, 6, 89, 100, 0, 34]
list4.sort()
print("list4 :", list4)
list5 = ["banana", "grapes", "mango", "apple"]
list5.sort(reverse=True)
print("list5 :", list5)

"""
"""
# write a python program to get all the even values from list
list6 = [45, 88, 567, 741, 44, 67, 64]
output = []

for val in list6:
    if val % 2 != 0:
        output.append(val)
    else:
        continue

print("output :", output)

"""