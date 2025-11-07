#29th oct-25
######################## Max, Min, sum of list values ##############nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn  vvvv v   v vvvvvv vv
list1 = [4, 7, 10, 50, 23, 45]

print("max value :", max(list1))  # max value : 50
print("min value :", min(list1))  # min value : 4
print("sum of values :", sum(list1))  # sum of values : 139

print("_" * 50)
###########################################################
# sorted function.
#sort is a method, where it modifies the original list.
#reverse also modifies the original list



# Increasing order
list2 = [6, 8, 9, 2, 1]
result2 = list(sorted(list2))  # [1, 2, 6, 8, 9]
print("sorted result :", result2)

# Decreasing order
result4 = list(sorted(list2, reverse=True))  # [9, 8, 6, 2, 1]
print("decreasing sorted result :", result4)

# reversed function
result3 = list(reversed(list2))
print("result3 :", result3)  # [1, 2, 9, 8, 6]

#############################################################
#difference between use of function and method is
#with method we use the .method e.x list1.sort()
#since function is individual entity we dont use .  , E.x sorted(list)