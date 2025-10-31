################################remove method############################
list_1=[2,3,4,6,7,0,-7,-55]
list_1.remove(0)
list_1.remove(4)
print("list_1:", list_1)

################################pop methods################333333333333
list_2= list_1.pop()
print("removed value :", list_2)
print("list_1 :",list_1)
###########################sorting#################
list_3= list(sorted(list_1, reverse=True))
print("sorted result in decreasing :", list_3)